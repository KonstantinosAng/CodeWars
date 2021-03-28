# see https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python


def high_and_low(numbers):
  n = [int(x) for x in numbers.split(" ")]
  return ' '.join(str(x) for x in [max(n), min(n)])


from TestFunction import Test
test = Test(None)
test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
test.assert_equals(high_and_low("1 -1"), "1 -1");
test.assert_equals(high_and_low("1 1"), "1 1");
test.assert_equals(high_and_low("-1 -1"), "-1 -1");
test.assert_equals(high_and_low("1 -1 0"), "1 -1");
test.assert_equals(high_and_low("1 1 0"), "1 0");        
test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
test.assert_equals(high_and_low("42"), "42 42");
