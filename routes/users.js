var express = require("express");
var router = express.Router();

/* GET users listing. */
router.get("/", function(req, res, next) {
  users = [
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
      id: 1,
      isEmployed: false
    }
  ];

  res.send(users);
});

module.exports = router;
