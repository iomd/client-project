// make folder
var fs = require('fs');
fs.mkdir('make_folder.js test folder',function(){
  fs.readFile('readMe.txt', 'utf8', function(err, data){
    fs.writeFile('writeMe.txt', data)
  });
});
