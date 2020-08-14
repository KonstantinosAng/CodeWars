// see https://www.codewars.com/kata/5846aaffdbb1b19d300001fb/train/javascript

const moment = require('moment');
function getDate(uts, loc) {
  return moment.unix(uts).format((formats[loc] || 'DD/MM/YYYY').toUpperCase());
}


console.log(getDate(1481020142, 'en-GB'), '06/12/2016');
console.log(getDate(1481020142, 'en-US'), '12/6/2016');
console.log(getDate(1481020142, 'de-DE'), '06.12.2016');
  