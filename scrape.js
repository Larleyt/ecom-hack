"use strict";

var request = require("request");
var cheerio = require("cheerio");

var LOOKBOOK_URL = "https://www.zalando.co.uk/men-street-style/?wmc=OSM_GC-AW16_1193_2_UK";

request(LOOKBOOK_URL, function(error, response, html) {
    if (!error && response.statusCode === 200) {
        var $ = cheerio.load(html);
        $("a.teaserBox > img").each(function() {
            console.log($(this).attr("src"));
        });

    }
});
