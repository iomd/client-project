const fs = require('fs');

// if exist then create folder
// if (!fs.existsSync('./SongTitle')) {
//   fs.mkdir('./SongTitle', (err) => {
//     if (err) throw err;
//     console.log('Directory Created')
//   });
// };

// if exist then remove folder
if (!fs.existsSync('./SongTitle')) {
  fs.rmdir('./SongTitle', (err) => {
    if (err) throw err;
    console.log('Directory Removed')
  });
};
