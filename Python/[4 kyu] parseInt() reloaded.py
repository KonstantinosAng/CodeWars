# see https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python

hashMap = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90} 
breakpoints = {'hundred': '00', 'thousand': '000', 'million': '000000'}
def parse_int(string):
  string = string.replace("-", " ").split(" ")
  if len(string) == 1: return hashMap[string[0]]
  retArray = []
  tempSum = 0
  counter = 0
  length = 1
  if 'hundred' in string: length = 3
  if 'thousand' in string: length = 4
  if 'million' in string: length = 7
  while counter < len(string):
    s = string[counter]
    if s != "" and s != 'and':
      if s in hashMap: 
        tempSum += hashMap[s]
      if s in breakpoints:
        tempSum = int(str(tempSum) + breakpoints[s])
      if len(str(tempSum)) >= length:
        retArray.append(tempSum)
        if length == 7: length = 4
        elif length == 4: length = 3
        else: length = 1
        tempSum = 0
    counter += 1
  return sum(retArray + [tempSum])
    


from TestFunction import Test

test = Test(None)

test.assert_equals(parse_int('one'), 1)
test.assert_equals(parse_int('twenty'), 20)
test.assert_equals(parse_int('two hundred forty-six'), 246)
test.assert_equals(parse_int('two hundred and forty-six'), 246)
test.assert_equals(parse_int('two thousand'), 2000)
test.assert_equals(parse_int('six hundred sixty-six thousand six hundred sixty-six'), 666666)
test.assert_equals(parse_int('two hundred thousand three'), 200003)