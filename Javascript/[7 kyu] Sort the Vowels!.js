// https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/javascript

function sortVowels(s) {
  if (typeof s === "number" || typeof s === "undefined") {
    return "";
  }
  return [...s]
    .map((letter) => {
      if (
        letter.toLowerCase() === "a" ||
        letter.toLowerCase() === "e" ||
        letter.toLowerCase() === "o" ||
        letter.toLowerCase() === "i" ||
        letter.toLowerCase() === "u"
      ) {
        letter = `|${letter}`;
      } else {
        letter = `${letter}|`;
      }
      return letter;
    })
    .join("\n");
}

console.log(sortVowels("Codewars"), "C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|");
console.log(sortVowels("Rnd Te5T"), "R|\nn|\nd|\n |\nT|\n|e\n5|\nT|");
console.log(sortVowels(1337), "");
console.log(sortVowels(undefined), "");
