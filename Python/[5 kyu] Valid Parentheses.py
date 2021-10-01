# see https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

def find_match(string, position, recursion=False):
  ret = False
  while position < len(string):
    if position == len(string)-1 and recursion and string[position] != ')':
      ret = False
      return ret, string, position
    if string[position] == ')':
      if recursion: 
        ret = True
        return ret, string, position
      else: 
        ret = False
        return ret, string, position
    if string[position] == '(':
      position += 1
      ret, string, position = find_match(string, position, recursion=True)
      if position == len(string) - 1: 
        return ret, string, position
    position += 1
  return ret, string, position


def valid_parentheses(string):
  if string.strip() == "": return True
  count1 = string.count('(')
  count2 = string.count(')')
  if count1 != count2: return False
  return find_match(string, 0)[0]



from TestFunction import Test
test = Test(None)   
test.assert_equals(valid_parentheses("  ("), False)
test.assert_equals(valid_parentheses(")test"), False)
test.assert_equals(valid_parentheses(""), True)
test.assert_equals(valid_parentheses("hi())("), False)
test.assert_equals(valid_parentheses("hi(hi)()"),True)
test.assert_equals(valid_parentheses("iynhjg(kdduvlhj(vi((xicbk(m)sg)vbcqe"), False)
test.assert_equals(valid_parentheses("e(bm)((v(qmgbx))d(no)"), False)
test.assert_equals(valid_parentheses("(giyhykvoh(ll)dwc(rgschlii(ydzfa)yqza)fn(hot)"), False)
