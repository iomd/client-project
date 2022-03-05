const fs = require('fs');
const rs = fs.createReadStream('../Template/TextFiles/sample_cue_points.txt');
const ws = fs.createWriteStream('./SongTitle/src/docs/sample_cue_points.txt');
rs.on('data', (dataChunk) => {
  ws.write(dataChunk);
});
