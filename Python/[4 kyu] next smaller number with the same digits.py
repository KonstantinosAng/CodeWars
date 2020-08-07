# see https://www.codewars.com/kata/5659c6d896bc135c4c00021e

def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))

from TestFunction import Test
Test = Test(None)
Test.it("Smaller numbers")
Test.assert_equals(next_smaller(907), 790)
Test.assert_equals(next_smaller(531), 513)
Test.assert_equals(next_smaller(135), -1)
Test.assert_equals(next_smaller(2071), 2017)
Test.assert_equals(next_smaller(414), 144)
Test.assert_equals(next_smaller(123456798), 123456789)
Test.assert_equals(next_smaller(123456789), -1)
Test.assert_equals(next_smaller(1234567908), 1234567890)