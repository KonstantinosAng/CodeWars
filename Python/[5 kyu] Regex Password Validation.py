# see https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python

regex="^(?!.*[<>%$';.!/?\-+_ /^\\\\/])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$"


from TestFunction import Test
test = Test(None)   

from re import search
test.describe("Basic tests")
test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
test.assert_equals(bool(search(regex, 'ghdfj32')), False)
test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
test.assert_equals(bool(search(regex, 'dsF43')), False)
test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
test.assert_equals(bool(search(regex, 'djI38D55')), True)
test.assert_equals(bool(search(regex, 'a2.d412')), False)
test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
test.assert_equals(bool(search(regex, '!fdjn345')), False)
test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
test.assert_equals(bool(search(regex, '123')), False)
test.assert_equals(bool(search(regex, 'abc')), False)
test.assert_equals(bool(search(regex, '123abcABC')), True)
test.assert_equals(bool(search(regex, 'ABC123abc')), True)
test.assert_equals(bool(search(regex, 'Password123')), True)
test.assert_equals(bool(search(regex, 'Yd5ej\\ek3B')), False)
