// https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/javascript


function permutations(string) {
  if (string.length < 2) { return [string] }
  let ret = []
  for (let i = 0; i < string.length; i++) {
    const char = string[i]
    if (string.indexOf(char) != i)
    continue
    const otherChars = string.slice(0, i) + string.slice(i + 1, string.length)
    for (const permutation of permutations(otherChars)) {
      ret.push(char+permutation)
    }
  }
  return ret
}


console.log(permutations('a'), ['a']);
console.log(permutations('ab').sort(), ['ab', 'ba'].sort());
console.log(permutations('aabb').sort(), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'].sort());