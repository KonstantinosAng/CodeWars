// see https://www.codewars.com/kata/526571aae218b8ee490006f4/solutions/javascript

var countBits = function(n) {
  var counts = 0; 
  n.toString(2).split("").map((digit) => {
    if (digit === '1') {counts++}
  });
  return counts
};