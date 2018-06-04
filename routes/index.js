var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.send({ isResponding: true});
});

router.get('/blah', function(req, res, next) {
    res.send({ isResponding: true, blah: 'yes'});
});

module.exports = router;
