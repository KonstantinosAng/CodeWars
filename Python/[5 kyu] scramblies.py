# see https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

def scramble(s1, s2):
  for c in set(s2):
    if s1.count(c) < s2.count(c):
      return False
  return True


from TestFunction import Test
test = Test(None)   

test.assert_equals(scramble('rkqodlw', 'world'),  True)
test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assert_equals(scramble('katas', 'steak'), False)
test.assert_equals(scramble('scriptjava', 'javascript'), True)
test.assert_equals(scramble('scriptingjava', 'javascript'), True)
test.assert_equals(scramble('mvybimhqldeymxbhs', 'vxsgxlzquqnuct'), False)