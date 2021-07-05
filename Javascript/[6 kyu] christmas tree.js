// https://www.codewars.com/kata/52755006cc238fcae70000ed/train/javascript

function christmasTree(height) {
  if (height === 0) { return "" }
  var ret = ''
  for (var i=0; i < height; i++) {
    // const j = 2*i + 1
    for (var j = 0; j < height - i - 1; j++) {
      ret += ' '
    }
    for (var j = 0; j < 2 * i + 1; j++) {
      ret += '*'
    }
    for (var j = 0; j < height - i - 1; j++) {
      ret += ' '
    }
    ret += '\n'
  }
  return ret.slice(0, ret.length-1)
}


console.log(JSON.stringify(christmasTree(0)), "\"\"")
console.log(JSON.stringify(christmasTree(1)), "\"*\"")
console.log(JSON.stringify(christmasTree(2)), "\" * \\n***\"")
console.log(JSON.stringify(christmasTree(3)), "\"  *  \\n *** \\n*****\"")
console.log(JSON.stringify(christmasTree(4)), "\"   *   \\n  ***  \\n ***** \\n*******\"")