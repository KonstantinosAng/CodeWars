// see https://www.codewars.com/kata/5a626fc7fd56cb63c300008c/train/javascript

function uncollapse(digits) {
  digitsMap = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero",
  ];
  index = 0;
  start = 0;
  returnString = [];
  while (index <= digits.length) {
    ret = digits.substring(start, index);
    if (digitsMap.includes(ret)) {
      returnString.push(ret);
      start = index;
    }
    index += 1;
  }
  return returnString.join(" ");
}

console.log(uncollapse("three"), "three");
console.log(uncollapse("eightsix"), "eight six");
console.log(uncollapse("fivefourseven"), "five four seven");
console.log(uncollapse("ninethreesixthree"), "nine three six three");
console.log(uncollapse("foursixeighttwofive"), "four six eight two five");
