# see https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

def longest_repetition(chars):
  if chars == "": return ("", 0)
  memoryDict = {}
  pointer = 0
  while pointer < len(chars) - 1:
    length = 1
    while chars[pointer] == chars[pointer + 1]:
      pointer += 1
      length += 1
      if not pointer < len(chars) - 1: break
    if chars[pointer] in memoryDict:
      if memoryDict[chars[pointer]][0] < length:
        memoryDict[chars[pointer]] = (length, pointer)
    else: memoryDict[chars[pointer]] = (length, pointer)
    pointer += 1
  maxLength = ('', 0, 0)
  for key, value in memoryDict.items():
    if value[0] > maxLength[1]: maxLength = (key, value[0], value[1])
    if value[0] == maxLength[1]:
      if value[1] < maxLength[2]:
        maxLength = (key, value[0], value[1])
  return maxLength[:2]
    


from TestFunction import Test
test = Test(None)

test.describe("Example Tests")

tests = [
    # [input, expected],
    ["aaaabb", ('a', 4)],
    ["bbbaaabaaaa", ('a', 4)],
    ["cbdeuuu900", ('u', 3)],
    ["abbbbb", ('b', 5)],
    ["aabb", ('a', 2)],
    ["ba", ('b', 1)],
    ["", ('', 0)],
]

for inp, exp in tests:
  test.assert_equals(longest_repetition(inp), exp)

string = """
:oa<z!yLr"CH$b"SXDZ^jtS:^sEi)a^u[i-_|-Kv]cR.mm(y_$C$[Tj\ylW&=|]NN,-}rSOIp;d!RJtRSj--m?_DQbr#DV"j_)m[XFOQ^X\jm.$by{zJNDLVs~cSnO^G<spD]<kNU:#nS;EfTh/KFC#!iL#IcUm}b;>GXx'-NdPqBPM%"P@M"^=ulOV(FFHMDn"}H.;H{PGE"ReV>;$$D'/e/-&*(DCcCgQ)]Z+c".uK][:CgR=wDB]Q$FUS>TTJcVh~W_ne\czK[kX/'w&m{/Kw[)FgOt$:gU(RXu,m-(H*'EziBtZMM~[SffrS+X(hGJ?p{[afuj-c>{]?q%,_A-i-S*^bHduVd_O\+gBlvBkhByNLmMSaFdfE%o^<NIVdiQ{<@"-&\kiR%U_[lx#$ZwRUrwnv.R,+L'!\W<p^O%]{FS!k,k^!K_gwRj$NOER|w~xGA@q<Qg?n(JYqu/&}u*P;!k{V]YCR~p}q]A$|UPN'@E-Hsf+d
"""

test.assert_equals(longest_repetition(string), ('m', 2))
