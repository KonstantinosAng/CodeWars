# see https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/solutions/python

from TestFunction import Test

def int32_to_ip(int32):
	if int32 == 0: return '0.0.0.0'
	binary = "{0:b}".format(int32)
	while len(binary) < 32: binary = '0' + binary
	step = len(binary)//4
	ipv4 = [int(binary[i:i+step], 2) for i in range(0, len(binary), step)]
	return '.'.join([str(x) for x in ipv4])

Test = Test(None)
Test.assert_equals(int32_to_ip(2154959208), "128.114.17.104") 
Test.assert_equals(int32_to_ip(0), "0.0.0.0")
Test.assert_equals(int32_to_ip(2149583361), "128.32.10.1")
Test.assert_equals(int32_to_ip(1046364997), "62.94.67.69")
