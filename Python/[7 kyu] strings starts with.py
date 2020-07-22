# see https://www.codewars.com/kata/5803a6d8db07c59fff00015f/solutions/python

from TestFunction import Test

def starts_with(st, prefix): 
    if prefix == "": return True
    if len(prefix) > len(st): return False
    if prefix in st and prefix[0] == st[0]: return True
    return False

Test(True).assert_result(starts_with("hello world!", "hello"))
Test(False).assert_result(starts_with("hello world!", "HELLO"))
Test(False).assert_result(starts_with("nowai", "nowaisir"))
Test(True).assert_result(starts_with("", ""))
Test(True).assert_result(starts_with("abc", ""))
Test(False).assert_result(starts_with("", "abc"))
Test(False).assert_result(starts_with("tzT44S(1`V@GI", "T4"))
Test(False).assert_result(starts_with("Cqy.x]p6dk~Vd'7		WcW&", "x]p6dk~Vd'7"))
Test(False).assert_result(starts_with('r^+">otE;Wl*j+J', '">otE;Wl'))
