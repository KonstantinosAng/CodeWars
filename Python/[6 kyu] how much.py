# see https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/train/python

from TestFunction import Test

def isInteger(number):
  if str(number).split(".")[1] == '0':
    return True
  else:
    return False

def howmuch(m, n):
  ret = []
  for i in range(min(m, n), max(m, n) + 1):
    c = (i - 1) / 9
    b = (i - 2) / 7
    if isInteger(c) and isInteger(b):
      ret.append([f"M: {i}", f"B: {int(b)}", f"C: {int(c)}"])
  return ret


test = Test(None)
test.assert_equals(howmuch(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
test.assert_equals(howmuch(1000, 1100), [["M: 1045", "B: 149", "C: 116"]])
test.assert_equals(howmuch(10000, 9950), [["M: 9991", "B: 1427", "C: 1110"]])
test.assert_equals(howmuch(0, 200), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]])
test.assert_equals(howmuch(2950, 2950), [])
test.assert_equals(howmuch(20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])