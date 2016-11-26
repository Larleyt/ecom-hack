"use strict";

var request = require("request");
var cheerio = require("cheerio");

var PALETTE_URL = "http://www.colourlovers.com/fashion/palettes";

request(PALETTE_URL, function(error, response, html) {
    if (!error && response.statusCode === 200) {
        var $ = cheerio.load(html);
        console.log($(".detail-row"));
        $(".detail-row a.palette span").each(function() {
            console.log($(this).attr("style"));
        });

    }
});