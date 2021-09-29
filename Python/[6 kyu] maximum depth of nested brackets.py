# see https://www.codewars.com/kata/60e4dfc1dc28e70049e2cb9d/train/python

from TestFunction import Test

def strings_in_max_depth(s):
  if "(" not in s or ")" not in s: return [s]
  m = 0
  count = 0
  ret = []
  for c in s:
    if c == "(": count += 1
    if c == ")": count -= 1
    if count > m: m = count
  count = 0
  word = ""
  for c in s:
    if c == "(": count += 1
    if c == ")": count -= 1
    if count == m:
      word += c
    else:
      if word != "":
        ret.append(word)
        word = ""
  return [x.replace("(", "") for x in ret]



test = Test(None)
test.describe("Example test cases")
test.it("basic test")
test.assert_equals(strings_in_max_depth("AA(XX((YY))(U))"), ["YY"])
test.assert_equals(strings_in_max_depth("((AAX(AB)(UP)F(Z))(HH))"),  ['AB', 'UP', 'Z'])
test.assert_equals(strings_in_max_depth("FB(TAIHJK(NZZCGDZXKF(SYMBLACQ)SBJMRFM)PRTRX(JCLYCOXIMOKGGIE)MWIOIJDCLXDSQFHK)WLVYSMNNHIGKR(MOIZLOT(RWMAVXSJQROHJ(GZURPPOQJVMYCE(VCPXSHXQ)LETIEWE(CBC)AAHEEO)NZHIGXBSJATXV)BSBYCMKFFAFZIK(KECNRQ)PIIQZGIDMLNQRQS)VGXXBYD"), ['VCPXSHXQ', 'CBC'])
test.assert_equals(strings_in_max_depth("AAA"), ["AAA"])
test.assert_equals(strings_in_max_depth(""), [""])