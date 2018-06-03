#!/bin/sh

# TAKE IN PARAMETERS
ENDPOINT=$1
FULL_ENDPOINT=http://localhost:3000/${ENDPOINT}

# EXECUTE LOGIC
NOT_EMPLOYED_USERS=$(curl -s ${FULL_ENDPOINT} | jq ' .users[] | select(."isEmployed"==false)')

# ASSESS RESULT
if [[ ${NOT_EMPLOYED_USERS} ]]; then
  echo 'Unemployed user(s) found:'
  echo ${NOT_EMPLOYED_USERS} | jq '"\(.name) (uid:\(.id))"'
  exit 1
else
  echo "All users are employed"
  exit 0
fi
