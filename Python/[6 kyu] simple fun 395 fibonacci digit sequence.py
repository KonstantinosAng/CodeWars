# see 

from TestFunction import Test

def find(a,b,n):
  if a == 0 and b == 0: return 0
  rv = f'{a}{b}'
  while len(rv) <= n:
    #rv += str(int(rv[-1]) + int(rv[-2]))
    rv = ''.join([rv, str(int(rv[-1]) + int(rv[-2]))])
  return int(rv[n])

test = Test(None)
test.assert_equals(find(7,8,9), 5)
test.assert_equals(find(0,0,1000000),0)
ss="78156112358134"
for i, ch in enumerate(ss):
    test.assert_equals(find(7,8,i),int(ch))

test.assert_equals(find(1,1,1580705454), 5)
test.assert_equals(find(0, 8, 1201006843), 3)
