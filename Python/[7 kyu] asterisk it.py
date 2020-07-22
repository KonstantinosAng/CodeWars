# see https://www.codewars.com/kata/5888cba35194f7f5a800008b/solutions/python

from TestFunction import Test

def asterisc_it(n): 
    if type(n) == list:
      n = "".join(str(s) for s in n)
    elif type(n) == int:
      n = str(n)
    else:
      pass
    ret = ''
    if len(n) == 1: return n
    for i in range(len(n) - 1):
      ret += n[i]
      if int(n[i])%2 == 0 and int(n[i+1])%2 == 0:
        ret += "*"
    return ret + n[-1]


Test('531270*8').assert_result(asterisc_it(5312708))
Test('96*8*2135').assert_result(asterisc_it(9682135))
Test('2*2*2*2').assert_result(asterisc_it(2222))
Test('1111').assert_result(asterisc_it(1111))
Test('9999').assert_result(asterisc_it(9999))
Test('0*0*0*0').assert_result(asterisc_it('0000'))
Test('8').assert_result(asterisc_it(8))
Test('2').assert_result(asterisc_it(2))
Test('0').assert_result(asterisc_it(0))
Test('14*6*4*6*8*67231').assert_result(asterisc_it([1, 4, 64, 68, 67, 23, 1]))
