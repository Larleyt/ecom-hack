"use strict";
var express = require("express");
var router = express.Router();

var multer = require("multer")
var fs = require("fs");
var PythonShell = require('python-shell');

var photoFile = require("../models/photo-file");

var upload = multer({
    dest: "./public/uploads/"
});

/* GET home page. */
router.get("/", function(req, res, next) {

    // get all the users
    photoFile.find({}, function(err, photos) {
        if (err) {
            throw err;
        }

        // object of all the users
        res.render("index", {
            title: "Express",
            photos: photos
        });
    });

});

router.post("/", upload.single("photo"), function(req, res) {
    console.log(res.file);
    var f = new photoFile({
        name: req.file.originalname,
        path: req.file.path
    });
    f.save(function(err) {
        if (err) {
            throw err;
        }
    });

    PythonShell.run("images.py", {args: [req.file.path]}, function (err, results) {
      if (err) {throw err;}
      results = JSON.parse(results);
      console.log(results.dominant_color);
    });

    res.redirect("/");
});

module.exports = router;
