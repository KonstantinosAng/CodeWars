// see https://www.codewars.com/kata/513e08acc600c94f01000001/solutions/javascript

function rgb2hex(color) {
  var hexadecimal = color.toString(16).toUpperCase();
  return hexadecimal.length == 1 ? "0" + hexadecimal : hexadecimal;
}

function rgb(r, g, b){
  if (r > 255) { r = 255}
  if (g > 255) { g = 255}
  if (b > 255) { b = 255}
  if (r < 0) { r = 0}
  if (g < 0) { g = 0}
  if (b < 0) { b = 0}
  return "" + rgb2hex(r) + rgb2hex(g) + rgb2hex(b);
}