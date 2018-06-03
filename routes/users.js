var express = require("express");
var router = express.Router();

/* GET users listing. */
router.get("/", function(req, res, next) {
  users = {
    users: [
      {
        name: "Stephen Geller",
        id: 1,
        isEmployed: true
      },
      {
        name: "Steve Hayes",
        id: 2,
        isEmployed: true
      },
      {
        name: "Jake Paul",
        id: 3,
        isEmployed: false
      },
      {
        name: "Beyonce Knowles",
        id: 4,
        isEmployed: false
      }
    ]
  };

  res.send(users);
});

router.get("/passing", function(req, res, next) {
  users = {
    users: [
      {
        name: "Stephen Geller",
        id: 1,
        isEmployed: true
      },
      {
        name: "Steve Hayes",
        id: 2,
        isEmployed: true
      },
      {
        name: "Jake Paul",
        id: 3,
        isEmployed: true
      },
      {
        name: "Beyonce Knowles",
        id: 4,
        isEmployed: true
      }
    ]
  };

  res.send(users);
});

router.get("/failing", function(req, res, next) {
  users = {
    users: [
      {
        name: "Stephen Geller",
        id: 1,
        isEmployed: true
      },
      {
        name: "Steve Hayes",
        id: 2,
        isEmployed: true
      },
      {
        name: "Jake Paul",
        id: 3,
        isEmployed: false
      },
      {
        name: "Beyonce Knowles",
        id: 4,
        isEmployed: false
      }
    ]
  };

  res.send(users);
});

module.exports = router;
