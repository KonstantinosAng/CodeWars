// see https://www.codewars.com/kata/545cedaa9943f7fe7b000048

function isPangram(string){
   let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
   let panagram = string.split("").map(function (letter) {
        if (letters.indexOf(letter.toLowerCase()) !== -1) {
               letters.splice(letters.indexOf(letter.toLowerCase()), 1);
        }
   })
   if (letters.length < 1) {
      return true
   }
      return false
}
