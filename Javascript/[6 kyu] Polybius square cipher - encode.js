// https://www.codewars.com/kata/542a823c909c97da4500055e/train/javascript

const encodeMap = "ABCDEFGHIIJKLMNOPQRSTUVWXYZ";

const findRow = (letter) => {
  return (
    Math.floor(
      (encodeMap[letter.toUpperCase().charCodeAt(0) - 65].charCodeAt(0) - 65) /
        5
    ) + 1
  );
};

const findCol = (letter) => {
  return (
    ((encodeMap[letter.toUpperCase().charCodeAt(0) - 65].charCodeAt(0) - 65) %
      5) +
    1
  );
};

function polybius(text) {
  return [...text]
    .map((letter) => {
      if (letter === " ") {
        return " ";
      }
      // if (letter.toLowerCase() === 'j' || letter.toLowerCase() === 'i')
      return `${findRow(letter)}${findCol(letter)}`;
    })
    .join("");
}

console.log(polybius("CODEWARS"), "1334141552114243", "CODEWARS");
console.log(
  polybius("POLYBIUS SQUARE CIPHER"),
  "3534315412244543 434145114215 132435231542",
  "POLYBIUS SQUARE CIPHER"
);
