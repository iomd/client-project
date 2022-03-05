const fs = require('fs');

const dir_names = {
  dir1:'/Users/icepitproductions/Desktop/scripts',
  dir2:'/Users/icepitproductions/Desktop/styles',
  dir3:'/Users/icepitproductions/Desktop/src',
  dir4:'/Users/icepitproductions/Desktop/src/img',
  dir5:'/Users/icepitproductions/Desktop/src/video',
  dir6:'/Users/icepitproductions/Desktop/src/audio',
  dir7:'/Users/icepitproductions/Desktop/src/audio/stems',
  dir8:'/Users/icepitproductions/Desktop/src/docs',
};

const file_names = {
  file1:'sample_cue_points.txt',
  file2:'client_email.csv',
  file3:'client_notes.csv',
  file4:'changelog.log',
  file5:'README.md',
}

const files_contents = {
  file1_contents:'text',
  file2_contents:'text',
  file3_contents:'text',
  file4_contents:'text',
  file5_contents:'text',
}

fs.mkdirSync(dir_names.dir1, 0o776);fs.mkdirSync(dir_names.dir2, 0o776);fs.mkdirSync(dir_names.dir3, 0o776);fs.mkdirSync(dir_names.dir4, 0o776);fs.mkdirSync(dir_names.dir5, 0o776);fs.mkdirSync(dir_names.dir6, 0o776);
fs.mkdirSync(dir_names.dir7, 0o776);
fs.mkdir(dir_names.dir8, (err)=>{

  if (err) {
    console.log(err.message);

  }else{
    fs.writeFileSync(`${dir_names.dir8}/${file_names.file1}`,`${files_contents.file1_contents}` );
    fs.writeFileSync(`${dir_names.dir8}/${file_names.file2}`,`${files_contents.file2_contents}` );
    fs.writeFileSync(`${dir_names.dir8}/${file_names.file3}`,`${files_contents.file3_contents}` );
    fs.writeFileSync(`${dir_names.dir8}/${file_names.file4}`,`${files_contents.file4_contents}` );
    fs.writeFileSync(`${dir_names.dir8}/${file_names.file5}`,`${files_contents.file5_contents}` );
  }
})
