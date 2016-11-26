// grab the things we need
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a schema
var photoFileSchema = new Schema({
  name: String,
  path: String,
});

// the schema is useless so far
// we need to create a model using it
var photoFile = mongoose.model("photoFile", photoFileSchema);

// make this available to our users in our Node applications
module.exports = photoFile;
