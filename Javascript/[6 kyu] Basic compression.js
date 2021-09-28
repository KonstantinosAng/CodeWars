// see https://www.codewars.com/kata/5914e068f05d9a011e000054/train/javascript

var compress = function (str) {
  map = [];
  newChar = str[0];
  count = 0;
  index = 0;
  while (index <= str.length) {
    if (newChar != str[index]) {
      map.push([count, newChar]);
      newChar = str[index];
      count = 1;
    } else {
      count += 1;
    }
    index += 1;
  }
  compressed = JSON.stringify(map);
  return compressed.length > str.length ? str : compressed;
};

var decompress = function (c) {
  try {
    ret = "";
    map = JSON.parse(c);
    for (const item of map) {
      ret += Array.apply(null, Array(item[0]))
        .map((x) => item[1])
        .join("");
    }
    return ret;
  } catch (e) {
    return c;
  }
};

var string1 = "aaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac";
var string2 = "abcde";
var c1 = '[[14,"a"],[1,"b"],[41,"a"],[1,"c"]]';
var c2 = "abcde";

// console.log(compress(string1), c1);
// console.log(compress(string2), c2);
console.log(decompress(c1), string1);
// console.log(decompress(c2), string2);
