// https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/javascript

function revrot(str, sz) {
  if (sz > str.length) { return "" }
  if (sz === 0) { return "" }
  var ret = '';
  var i = 0;
  var j = sz;
  var chunks = []
  while (i <= str.length) {
    chunks.push(str.slice(i, j))
    i += sz;
    j += sz
  }
  chunks.map(chunk => {
    if (chunk.length !== sz) {
    } else {
      if ([...chunk].map(str => parseInt(str) ** 2).reduce((a, b) => a + b, 0) % 2 === 0) {
        ret += [...chunk].reverse().join('')
      } else {
        ret += chunk.slice(1) + chunk.charAt(0)
      }
    }
  })
  return ret
}


console.log(revrot("123456987654", 6)) // --> "234561876549"
console.log(revrot("123456987653", 6)) // --> "234561356789"
console.log(revrot("66443875", 4)) // --> "44668753"
console.log(revrot("66443875", 8)) // --> "64438756"
console.log(revrot("664438769", 8)) // --> "67834466"
console.log(revrot("123456779", 8)) // --> "23456771"
console.log(revrot("", 8)) // --> ""
console.log(revrot("123456779", 0)) // --> "" 
console.log(revrot("563000655734469485", 4)) // --> "0365065073456944"