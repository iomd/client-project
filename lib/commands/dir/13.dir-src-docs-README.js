const fs = require('fs');
const rs = fs.createReadStream('../Template/TextFiles/README.md');
const ws = fs.createWriteStream('./SongTitle/src/docs/README.md');
rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
