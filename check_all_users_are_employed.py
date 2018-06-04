#!/usr/bin/env python
import sys
import urllib2
import json

# TAKE IN PARAMETERS
if len(sys.argv) == 1:
    print "please pass in an endpoint, for example:"
    print "$ %s [users OR users/passing OR users/failing]" % sys.argv[0]
    sys.exit(1)
else:
    first_argument = sys.argv[1]
    endpoint = first_argument
    full_endpoint = 'http://localhost:3000/%s' % endpoint


# EXECUTE LOGIC
def check_for_unemployed_users(array_of_users):
    unemployed_users = filter(lambda x : x["isEmployed"] == False, array_of_users)
    return unemployed_users

def __main__():
    contents = urllib2.urlopen(full_endpoint).read()
    users = json.loads(contents)['users']
    unemployed_users = check_for_unemployed_users(users)
    assess_response(unemployed_users)



# ASSESS RESULT

def assess_response(unemployed_users):
    if unemployed_users:
        print 'Unemployed user(s) found:'
        for user in unemployed_users:
            print "%s (uid: %s)" % (user['name'], user['id'])
        sys.exit(1)
    else:
        print 'All users employed!'



if __name__ == '__main__':
    __main__()
