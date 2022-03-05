var fs = require('fs');

fs.mkdir('stuff',function(){
  fs.readFile('readMe.txt', 'utf8', function(err, data){
    fs.writeFile('writeMe.txt', data)
  });
});


// read/write to file
//var fs = require('fs');
//var readMe = fs.readFileSync('readMe.txt', 'utf8');
//fs.writeFileSync('writeMe.txt', readMe);
