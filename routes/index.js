/* jshint ignore:start */
var express = require('express');
var router = express.Router();
var request = require('request');
var querystring = require('qs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {
    title: ''
  });
});

module.exports = router;
/* jshint ignore:end */
