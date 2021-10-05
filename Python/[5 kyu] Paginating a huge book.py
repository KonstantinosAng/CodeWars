# see https://www.codewars.com/kata/55905b7597175ffc1a00005a/train/python

def page_digits(pages):
  nDigits = len(str(pages))
  if nDigits == 1: return pages
  retArray = [9]
  for x in range(1, nDigits):
    digits = (pages - int(x*'9'))*(x+1) if nDigits <= x + 1 else int('9'+'0'*x)*(x+1)
    retArray.append(digits)
  return sum(retArray)



from TestFunction import Test

test = Test(None)
test.describe("Sample tests")
test.it("Tests")
test.assert_equals(page_digits(4), 4)
test.assert_equals(page_digits(10), 11)
test.assert_equals(page_digits(12), 15)
test.assert_equals(page_digits(20), 31)
test.assert_equals(page_digits(100), 192)
test.assert_equals(page_digits(101), 195)
