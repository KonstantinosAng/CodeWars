# see https://www.codewars.com/kata/5629db57620258aa9d000014/train/python

from TestFunction import Test


def mix(s1, s2):
  lowercase = 'abcdefghijklmnopqrstuvwxyz'
  count1 = {}
  count2 = {}
  ret = []
  for letter in lowercase:
    count1[letter] = s1.count(letter) 
    count2[letter] = s2.count(letter)
  for val1, val2 in zip(count1, count2):
    if count1[val1] > 1 or count2[val2] > 1:
      if count1[val1] > count2[val2]:
        ret.append('1:' + count1[val1]*val1 + '/')
      elif count1[val1] < count2[val2]:
        ret.append('2:' + count2[val2]*val2 + '/')
      else:
        ret.append('=:' + count2[val2]*val2 + '/')
  ret = sorted(ret, key=len, reverse=True)
  pointer = 0
  flip = True
  while flip:
    flip = False
    while pointer < len(ret) - 1:
      if len(ret[pointer]) == len(ret[pointer+1]):
        tmp = sorted([ret[pointer], ret[pointer+1]])
        if not ret[pointer] == tmp[0]:
          flip = True
        ret.pop(pointer)
        ret.pop(pointer)
        ret.insert(pointer, tmp[0])
        ret.insert(pointer + 1, tmp[1])
      pointer += 1
    pointer = 0
  return "".join(x for x in ret)[:-1]

test = Test(None)
test.describe("Mix")
test.it("Basic Tests")
test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
test.assert_equals(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
test.assert_equals(mix("codewars", "codewars"), "")
test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
