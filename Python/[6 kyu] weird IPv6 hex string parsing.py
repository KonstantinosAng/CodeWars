# see https://www.codewars.com/kata/5f5bc8a04e485f002d85b303/train/python

from TestFunction import Test

def parse_IPv6(iPv6):
  # split IP
  arr = [iPv6[x:x+4] for x in range(0, int(len(iPv6)/5)*5+1, 5)]
  sums = []
  for item in arr:
    digits = [x for x in item]
    s = 0
    for digit in digits:
      d = int(str('0x'+digit), 16)
      s += d
    sums.append(s)
  return "".join(str(x) for x in sums)
    

test = Test(None)
test.describe("Parse IPv6")
test.describe("basic tests")
test.assert_equals(parse_IPv6("1234:5678:9ABC:D00F:1111:2222:3333:4445"), "10264228481217")
test.assert_equals(parse_IPv6("5454:FBFD:9ABC:AAAA:FFFF:2222:FBDE:0101"), "18544240608532")
test.assert_equals(parse_IPv6("0000:0000:0000:0000:0000:0000:0000:0000"), "00000000")
test.assert_equals(parse_IPv6("FFFF:FFFF:BBBB:CCCC:1212:AABC:0000:1111"), "6060444864304")
test.assert_equals(parse_IPv6("ACDD-0101-9ABC-AAAA-FFFF-2222-FBDE-ACCC"), "48242406085346")
test.assert_equals(parse_IPv6("5454rFBFDr9ABCrAA0ArFAFFr2222rFBDEr0101"), "18544230558532")
test.assert_equals(parse_IPv6("F234#5678#9ABC#D00F#1111#2222#3333#4485"), "24264228481221")
