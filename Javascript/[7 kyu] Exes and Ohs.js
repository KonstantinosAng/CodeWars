// see https://www.codewars.com/kata/55908aad6620c066bc00002a

function XO(str) {
   var xs = 0;
   var os = 0;
   let arr = str.split("").map(function (val) {
        if (val.toLowerCase() === 'x') {
               xs++;
        }
        if (val.toLowerCase() === 'o') {
               os++;
        }
   });
   if (xs === os) {
        return true
   } else {
        return false
   }
}
