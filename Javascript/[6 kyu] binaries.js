// see https://www.codewars.com/kata/5d98b6b38b0f6c001a461198/train/javascript

function code(str) {
  return [...str]
    .map((digit) => {
      k = (digit >>> 0).toString(2).length;
      ret = "";
      for (let i = 0; i < k - 1; i++) {
        ret += "0";
      }
      ret += "1" + (digit >>> 0).toString(2);
      return ret;
    })
    .join("");
}

function decode(str) {
  start = 0;
  index = 0;
  digits = [];
  while (index < str.length) {
    if (str[index] === "1") {
      length = 2 * (index - start + 1);
      digit = str.substring(start, start + length);
      digits.push(digit);
      start += digit.length;
      index = start;
    } else {
      index += 1;
    }
  }
  return digits
    .map((digit) => {
      return parseInt(digit.substring(digit.length / 2), 2);
    })
    .join("");
}

// console.log(decode("001101001101001101101010"), "555000");

// console.log(code("62"), "0011100110");
// console.log(code("0"), "10");
// console.log(code("1"), "11");
// console.log(code("2"), "0110");
// console.log(code("3"), "0111");
// console.log(code("4"), "001100");
// console.log(code("5"), "001101");
// console.log(code("6"), "001110");
// console.log(code("7"), "001111");
// console.log(code("8"), "00011000");
// console.log(code("1520"), "11001101011010");
// console.log(code("10111213"), "11101111110110110111");
// console.log(code("55337700"), "001101001101011101110011110011111010");
// console.log(
//   code("1119441933000055"),
//   "1111110001100100110000110011000110010111011110101010001101001101"
// );
// console.log(code("69"), "00111000011001");
// console.log(code("86"), "00011000001110");
// console.log(
//   code("55500011144466666699919777777"),
//   "10001111001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100011101111100011001000110000001100000111100111101110111001100001100011001100011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111"
// );
// console.log(decode("10001111"), "07");
// console.log(decode("11001101011010"), "1520");
// console.log(decode("00111000011001"), "69");
// console.log(decode("11101111110110110111"), "10111213");
// console.log(
//   decode(
//     "001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100"
//   ),
//   "444666333666777444"
// );
// console.log(
//   decode(
//     "01110111110001100100011000000110000011110011110111011100110000110001100110"
//   ),
//   "33198877334422"
// );
// console.log(
//   decode(
//     "0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111"
//   ),
//   "55500011144466666699919777777"
// );
// console.log(
//   decode(
//     "01110111011111000110010011110011110011110011110011110011110111011101110110011001100110011001101111111010101100011001000110000001100000011000"
//   ),
//   "3331977777733322222211100019888"
// );
// console.log(
//   decode(
//     "10001111001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100011101111100011001000110000001100000111100111101110111001100001100011001100011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111"
//   ),
//   "55500011144466666699919777777"
// );
