const fs = require('fs');
const rs = fs.createReadStream('admin/tasks/copy & paste/readMe.txt');
const ws = fs.createWriteStream('admin/tasks/copy & paste/writeMe.txt');

rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
