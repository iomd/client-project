const fs = require('fs');
const rs = fs.createReadStream('../Template/TextFiles/client_email.csv');
const ws = fs.createWriteStream('./SongTitle/src/docs/client_email.csv');
rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
