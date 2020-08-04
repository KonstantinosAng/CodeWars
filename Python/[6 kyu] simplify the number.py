# see https://www.codewars.com/kata/5800b6568f7ddad2c10000ae/solutions/python

from TestFunction import Test

def simplify(number): 
  rv = ''
  for i, s in enumerate(str(number)):
    if s != '0':
      if i == len(str(number))-1:
        rv += s
      else:
        rv += s + f'*{10**(len(str(number))-i-1)}'
      rv += '+'
  return rv[:-1]


test = Test(None)
test.assert_equals(simplify(8964631), "8*1000000+9*100000+6*10000+4*1000+6*100+3*10+1")
test.assert_equals(simplify(56),"5*10+6")
test.assert_equals(simplify(999),"9*100+9*10+9")
test.assert_equals(simplify(11), "1*10+1")
test.assert_equals(simplify(991), "9*100+9*10+1")
test.assert_equals(simplify(47), "4*10+7")
test.assert_equals(simplify(234), "2*100+3*10+4")
test.assert_equals(simplify(196587), "1*100000+9*10000+6*1000+5*100+8*10+7")        
test.assert_equals(simplify(660), "6*100+6*10")
test.assert_equals(simplify(600), "6*100")
test.assert_equals(simplify(9090), "9*1000+9*10")
test.assert_equals(simplify(10104),"1*10000+1*100+4")
test.assert_equals(simplify(80008), "8*10000+8")
test.assert_equals(simplify(90000), "9*10000")
test.assert_equals(simplify(0), "")
