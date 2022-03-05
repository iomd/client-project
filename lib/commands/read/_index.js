const fs = require('fs');
const path = require('path');

// READ FILE FROM DIRECTORY
fs.readFile(path.join(__dirname, '../Template/TextFiles', 'sample_cue_points.txt'), (err, data) => {
  if (err) throw err;
  //console.log(data.toString());

  // WRITE FILE TO DIRECTORY
  fs.writeFile(path.join(__dirname, 'files', 'sample_cue_points.txt'), 'WRITE', (err) => {
    if (err) throw err;
    //console.log(data.toString());

    // APPEND (add to) FILE TO DIRECTORY
    fs.appendFile(path.join(__dirname, 'files', 'sample_cue_points.txt'), '\n\APPEND2', (err, data) => {
      if (err) throw err;
      //console.log(data.toString());
    });
  });
});

// console.log('Still too fast!!');

// stopped @min 13 https://youtu.be/yQBw8skBdZU?list=PL0Zuz27SZ-6PFkIxaJ6Xx_X46avTM1aYw