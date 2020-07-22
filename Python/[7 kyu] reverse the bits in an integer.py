# see https://www.codewars.com/kata/5959ec605595565f5c00002b/solutions/python

from TestFunction import Test, Tester

def reverse_bits(n):
  return int(str(bin(n).replace("0b", ""))[::-1], 2)

Test(267).assert_result(reverse_bits(417))
Test(417).assert_result(reverse_bits(267))
Test(0).assert_result(reverse_bits(0))
Test(1087).assert_result(reverse_bits(2017))
Test(1023).assert_result(reverse_bits(1023))
Test(1).assert_result(reverse_bits(1024))