# see https://www.codewars.com/kata/55983863da40caa2c900004e/train/python


from itertools import permutations

""" def next_bigger(n):
  m = int(''.join([str(y) for y in reversed(sorted([int(x) for x in str(n)]))]))
  if m == n: return -1
  if str(n)[-1] == '0': return int(str(n)[:-2] + str(n)[-1] + str(n)[-2])
  for x in permutations([int(x) for x in str(n)]):
    rv = int(''.join([str(y) for y in x]))
    if rv > n: return rv
  return -1 """


import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

from TestFunction import Test
Test = Test(None)
# Test.assert_equals(next_bigger(12),21)
# Test.assert_equals(next_bigger(513),531)
# Test.assert_equals(next_bigger(2017),2071)
# Test.assert_equals(next_bigger(414),441)
# Test.assert_equals(next_bigger(144),414)
# Test.assert_equals(next_bigger(123456789),123456798)
# Test.assert_equals(next_bigger(9876543210),-1)
# Test.assert_equals(next_bigger(9999999999),-1)
# Test.assert_equals(next_bigger(1234567980),1234567908)
# Test.assert_equals(next_bigger(59884848459853),59884848483559)
# Test.assert_equals(next_bigger(559260176761),559260171667)
Test.assert_equals(next_bigger(989999999999),998999999999)
