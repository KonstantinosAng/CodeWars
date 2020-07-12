// see https://www.codewars.com/kata/5526fc09a1bbd946250002dc/solutions/javascript

function findOutlier(integers){
  var odds = 0;
  var evens = 0;
  var even = false;
  var odd = false;
  var ret;
  for (let i=0;i<integers.length;i++) {
   if (integers[i]%2 === 0) {
      var even_number = integers[i];
      evens++;
    } else {
      var odd_number = integers[i];
      odds++;
    }
    if (even) {
       ret = even_number;
    }
    if (odd) {
      ret = odd_number;
    }
    if (ret !== undefined) { break }
    if (evens == 2) {
      odd = true;
    }
    if (odds == 2) {
      even = true;
    } 
  }
  if (odd) {
    return odd_number
  } else { 
    return even_number
  }
}