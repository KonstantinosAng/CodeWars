// https://www.codewars.com/kata/56f1c6034d0c330e4a001059/train/javascript

var generateColor = function() {
  const characters = '0123456789abcdef';
  var ret = '#'
  for (var i = 0; i < 6; i++) {
    ret += characters.charAt(Math.floor(Math.random() * 15))
  }
  return ret
};


console.log(generateColor())
console.log(generateColor())
console.log(generateColor())
console.log(generateColor())
console.log(generateColor())
console.log(generateColor().substring(0, 1), "#")