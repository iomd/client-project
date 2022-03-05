const fs = require('fs');
const rs = fs.createReadStream('../Template/TextFiles/changelog.log');
const ws = fs.createWriteStream('./SongTitle/src/docs/changelog.log');
rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
