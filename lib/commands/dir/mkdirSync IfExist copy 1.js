// node js make directory

var fs = require('fs');
var dir = './tmp';
if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
}
