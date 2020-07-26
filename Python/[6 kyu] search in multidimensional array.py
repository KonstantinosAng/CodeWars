# see https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/solutions/python
from TestFunction import Test

def recursive(seq, value):
  for val in seq:
    if type(val) == list or type(val) == tuple:
      if recursive(val, value):
        return True
    else:
      if val == value:
        return True
  return False

def locate(seq, value):
  if value in seq: return True
  i = 0
  while i <= len(seq) - 1:
    if type(seq[i]) == list or type(seq[i]) == tuple:
      if recursive(seq[i], value):
        return True
    if seq[i] == value: return True
    i += 1
  return False

Test = Test(None)
Test.assert_equals(locate(['a','b',['c','d',['e']]],'a'), True)
Test.assert_equals(locate(['a','b',['c','d',['e']]],'d'), True)
Test.assert_equals(locate(['a','b',['c','d',['e']]],'e'), True)
Test.assert_equals(locate(['a','b',['c','d',['e']]],'f'), False)
Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'e4'), True)
Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e4',['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e14']]]]]],]]]]]]]]],]]],'e'), True)
Test.assert_equals(locate([["'i}RZMK.''i}RZMK.'", ["'kA1''kA1'"], "'WQ3z2''WQ3z2'", "'%x''%x'"], [['mf', ["'cF~2mKs''cF~2mKs'", ["'f''f'", ['ok{pgR', "'M:y''M:y'", 'PK+!{', [['4bj&?t']], ['4:.', "']'']'", [')Uz', "'4''4'"], ['x', "'LaB@h6''LaB@h6'", 'r*n{3']]], ['1^', ':ZU', [[], [], [], '#>6T<', ["'}Lb*?r`''}Lb*?r`'", "'m!2#im}''m!2#im}'", '5~!L', "'duxhnMz''duxhnMz'"]], "'N''N'", ["';'';'", ['FzguAD']]], '<w<JFi&'], 'N+.Q/.,'], 'v_sd|k', [[["'woM[z''woM[z'", 't"=GFc_', 'W', ["'[1fV>5c''[1fV>5c'", 'Nf8c<$1', ['Bpjg_s:', "'gAK''gAK'", "'SQ[OH<''SQ[OH<'"]]], 'c<SN`o', "'z)fI>8''z)fI>8'", [[["'w3Le''w3Le'"], ')4fuYTd', "'K''K'"], 'Uo', [["'.Q/5LE''.Q/5LE'", '\'"SV;Dh\'\'"SV;Dh\'', 'aXc'], "'?034)V''?034)V'", [], '>4dhe', "'"]]]]]], [['aP&', 'KekHi'], '"c+\'R""c+\'R"'], '%b'], 'c<SN`o'), True)
Test.assert_equals(locate([['mf', ["'cF~2mKs''cF~2mKs'", ["'f''f'", ['ok{pgR', "'M:y''M:y'", 'PK+!{', [['4bj&?t']], ['4:.', "']'']'", [')Uz', "'4''4'"], ['x', "'LaB@h6''LaB@h6'", 'r*n{3']]], ['1^', ':ZU', [[], [], [], '#>6T<', ["'}Lb*?r`''}Lb*?r`'", "'m!2#im}''m!2#im}'", '5~!L', "'duxhnMz''duxhnMz'"]], "'N''N'", ["';'';'", ['FzguAD']]], '<w<JFi&'], 'N+.Q/.,'], 'v_sd|k', [[["'woM[z''woM[z'", 't"=GFc_', 'W', ["'[1fV>5c''[1fV>5c'", 'Nf8c<$1', ['Bpjg_s:', "'gAK''gAK'", "'SQ[OH<''SQ[OH<'"]]], 'c<SN`o', "'z)fI>8''z)fI>8'", [[["'w3Le''w3Le'"], ')4fuYTd', "'K''K'"], 'Uo', [["'.Q/5LE''.Q/5LE'", '\'"SV;Dh\'\'"SV;Dh\'', 'aXc'], "'?034)V''?034)V'", [], '>4dhe', "'"]]]]]], 'c<SN`o'), True)
Test.assert_equals(locate([["nl>'H", "'4~yNq''4~yNq'", ["'21''21'", "'VGHj''VGHj'", 'CT/Qn']], 'i5?<r', "'rj''rj'", "'tF''tF'"], 'CT/Qn'), True)
Test.assert_equals(locate(["nl>'H", "'4~yNq''4~yNq'", ["'21''21'", "'VGHj''VGHj'", 'CT/Qn']], 'CT/Qn'), True)
