# Nagios Check Tutorial

Created as part of an 'intro to Nagios checks' class.

## How to use:

First, you'll need to set up the local server that our check will be querying:

```bash
$ git clone git@github.com:stephengeller/nagios-check-tutorial.git
$ cd nagios-check-tutorial
$ npm install # installs dependencies
$ npm start # starts the server
```

To launch basic json sever instead:
```bash
$ npm i -g json-server
$ json-server json-server.json

```

Once the server is up, you can run either the python (`check_all_users_are_employed.py`) or shell (`check_all_users_are_employed.sh`) script _with an argument_ to verify whether users in our fake company are actually employed to the company or not.

```bash
$ ./check_all_users_are_employed.sh users
$ echo $? # This will show you whether the check passes or failed based on the exit code
```

The currently configured endpoints are:

* `users`
* `users/passing`
* `users/failing`
