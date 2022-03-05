# Instructions

## writeMe.js

writes contents of 'readME.txt' to 'writeME.txt'

```javascript
var fs = require('fs');
var readMe = fs.readFileSync('readMe.txt', 'utf8');
fs.writeFileSync('writeMe.txt', readMe);

```

---
