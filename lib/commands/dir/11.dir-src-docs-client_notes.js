const fs = require('fs');
const rs = fs.createReadStream('../Template/TextFiles/client_notes.csv');
const ws = fs.createWriteStream('./SongTitle/src/docs/client_notes.csv');
rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
