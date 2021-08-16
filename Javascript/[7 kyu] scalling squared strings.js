// https://www.codewars.com/kata/56ed20a2c4e5d69155000301/train/javascript

function scale(strng, k, n) {
  if (strng === "") {
    return ""
  } else {
    let ret = '';
    str = strng.split('\n')
    len = str.length;
    for (var sent of str) {
      for (var j=0;j<n;j++) {
        let l = 0;
        while (l < len) {
          for (var i=0;i<k;i++) {
            ret += sent.charAt(l);
          }
          l+=1;
        }
        ret += '\n';
      }
    }
    return ret.substring(0, ret.length - 1);
  }
}


var a = "abcd\nefgh\nijkl\nmnop";
var r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp";
console.log(scale(a, 2, 3))
// console.log(scale(a, 2, 3), r);
// console.log(scale("", 5, 5), "");
// console.log(scale("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH");