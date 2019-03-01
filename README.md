# Nagios Check Tutorial

Created as part of an 'intro to Nagios checks' class.

## How to use:

First, you'll need to set up the local server that our check will be querying:

```bash
$ git clone git@github.com:stephengeller/nagios-check-tutorial.git
$ cd nagios-check-tutorial
$ npm install # installs dependencies
$ npm start # starts the ndoe server
$ npm run json-only # starts a json-only server, serving the json-server.json file
```

#### How to query localhost server:
Find local ip:

- run `ifconfig | grep -A 5 en0`
- Copy the number after inet (possibly 10.10.x.x)
 - Then run curl against that ip instead of localhost, eg curl 10.10.10.140:3000/users


Once the server is up, you can run either the python (`check_all_users_are_employed.py`) or shell (`check_all_users_are_employed.sh`) script _with an argument_ to verify whether users in our fake company are actually employed to the company or not.

```bash
$ ./check_all_users_are_employed.sh users
$ echo $? # This will show you whether the check passes or failed based on the exit code
```

The currently configured endpoints are:

* `users`
* `users/passing`
* `users/failing`
