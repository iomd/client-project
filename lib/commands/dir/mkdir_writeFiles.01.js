const fs = require('fs');

// directories
const dirnames = {
  sync1:"Scripts",
  sync2:"Styles",
  sync3:"src",
  sync4:"src/img",
  sync5:"src/video",
  sync6:"src/audio",
  sync7:"src/audio/stems",
  sync8:"src/docs",
};

// directories
fs.mkdirSync(dirnames.sync1, 0o776);
fs.mkdirSync(dirnames.sync2, 0o776);
fs.mkdirSync(dirnames.sync3, 0o776);
fs.mkdirSync(dirnames.sync4, 0o776);
fs.mkdirSync(dirnames.sync5, 0o776);
fs.mkdirSync(dirnames.sync6, 0o776);
fs.mkdirSync(dirnames.sync7, 0o776);
fs.mkdirSync(dirnames.sync8, 0o776);

// define file contents
const sample_cue_points = "1"
const client_email = "1"
const client_notes = "1"
const changelog = "1"
const README = "1"

// write file contents
fs.writeFileSync(`${dirnames.sync8}/sample_cue_points.txt`,`${sample_cue_points}` );
fs.writeFileSync(`${dirnames.sync8}/client_email.csv`,`${client_email}` );
fs.writeFileSync(`${dirnames.sync8}/client_notes.csv`,`${client_notes}` );
fs.writeFileSync(`${dirnames.sync8}/changelog.log`,`${changelog}` );
fs.writeFileSync(`${dirnames.sync8}/README.md`,`${README}` );
