#!/usr/bin/env python
import sys
import urllib2
import json

# TAKE IN PARAMETERS
if len(sys.argv) == 1:
    print "please pass in an endpoint, for example:"
    print "$ %s [users OR users/passing OR users/failing]" % sys.argv[0]
    sys.exit(1)

first_argument = sys.argv[1]
endpoint = first_argument
full_endpoint = 'http://localhost:3000/%s' % endpoint


# EXECUTE LOGIC
def check_for_unemployed_users(array_of_users):
    unemployed_users = filter(lambda x : x["isActive"] == False, array_of_users)
    return unemployed_users


def __main__():
    try:
        contents = urllib2.urlopen(full_endpoint)
        users = json.loads(contents.read())
        unemployed_users = check_for_unemployed_users(users)
        assess_response(unemployed_users)
    except urllib2.URLError as e:
        print 'Bad response from server: %s' % e


# ASSESS RESULT


def assess_response(unemployed_users):
    if unemployed_users:
        print 'Unemployed user(s) found:'
        for user in unemployed_users:
            print "%s %s (uid: %s)" % (user['name']['first'], user['name']['last'], user['_id'])
        sys.exit(1)
    else:
        print 'All users employed!'


if __name__ == '__main__':
    __main__()
