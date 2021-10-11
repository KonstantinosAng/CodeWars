# see https://www.codewars.com/kata/5b883cdecc7c03c0fa00015a/train/python

f=lambda u:[i*sum(map(ord,u))%256 for i in[1,2,3,4]]

from TestFunction import Test
test = Test(None)
test.assert_equals(f('www.codewars.com'), [88, 176, 8, 96])
test.assert_equals(f('www.starwiki.com'), [110, 220, 74, 184])
test.assert_equals(f('www.winnerss.win'), [136, 16, 152, 32])