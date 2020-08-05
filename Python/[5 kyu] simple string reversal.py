# see https://www.codewars.com/kata/5a71939d373c2e634200008e/train/python

def solve(s):
  rv = ''
  spaces = [i for i, c in enumerate(s) if c == ' ']
  temp = s[::-1].replace(" ", "")
  j = 0
  for i, c in enumerate(temp):
    if i+j in spaces:
      rv += ' '
      j += 1
    rv += c
  if s[-1] == ' ': return rv + ' '
  return rv 


from TestFunction import Test
Test = Test(None)
Test.it("Basic tests")
Test.assert_equals(solve("codewars"),"srawedoc")
Test.assert_equals(solve("your code"),"edoc ruoy")
Test.assert_equals(solve("your code rocks"),"skco redo cruoy")
Test.assert_equals(solve("i love codewars"),"s rawe docevoli")
Test.assert_equals(solve("d d jy pi s lbo y utfbyz s nttldgynrnb qfw tfnfogm c tawwzftnhz jxpvp u plp luabfsz wbqc g le owqvurz vpq b m zzs vh p z zaapdpnn s v scda sjt tpfaf tt khe zrxf vy mzc uu wtp j nj eouwb hnzxu y gb uki "),"i k ub gy u xzn h bwuoej n jptwuuczmyv fxr zehkttf a fpttjsadcs vsnnp d paa zzphvsz zmbq p vz ruvqwoe lgc q b wzs fb a u lplpupvp x j zhnt fzw watcm go fnf twfq bn rny gd ltt n sz ybftu yobls i py jdd ")