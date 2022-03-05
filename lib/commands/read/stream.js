const fs = require('fs');
const rs = fs.createReadStream('./files/file.txt');
const ws = fs.createWriteStream('./files/newfile.txt');

rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
