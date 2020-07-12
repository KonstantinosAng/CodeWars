// see https://www.codewars.com/kata/56a5d994ac971f1ac500003e/solutions/javascript

function longestConsec(strarr, k) {
  var max = 0;
  var ret = '';
  for (let i = 0; i < strarr.length - k+1 ; i++) {
    var s = '';
    for (let j=i;j<=i+k-1;j++) {
      s += strarr[j];
    }
    if (s.length > max) {
      ret=s;
      max = s.length;
    }
  }
  return ret  
}