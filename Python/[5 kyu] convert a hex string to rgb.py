# see https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python

from TestFunction import Test
  
def hex_string_to_RGB(hex_string): 
  hex_string = hex_string.replace("#", "")
  r = int(hex_string[:2], 16)
  g = int(hex_string[2:4], 16)
  b = int(hex_string[4:], 16)
  return {'r': r, 'g': g, 'b': b}

test = Test(None)
test.assert_equals(hex_string_to_RGB("#FF9933"), {'r':255, 'g':153, 'b':51})
test.assert_equals(hex_string_to_RGB("#beaded"), {'r':190, 'g':173, 'b':237})
test.assert_equals(hex_string_to_RGB("#000000"), {'r':0, 'g':0, 'b':0})
test.assert_equals(hex_string_to_RGB("#111111"), {'r':17, 'g':17, 'b':17})
test.assert_equals(hex_string_to_RGB("#Fa3456"), {'r':250, 'g':52, 'b':86})
