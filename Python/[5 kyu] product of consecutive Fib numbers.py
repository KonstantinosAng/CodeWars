# see https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

fib_cache = {0: 0, 1: 1}
def get_fib_number(n):
  if n in fib_cache:
    return fib_cache[n]
  fib_cache[n] = result = get_fib_number(n-1) + get_fib_number(n-2)
  return result

def productFib(prod):
  counter = 0
  flag = True
  while flag:
    a, b = get_fib_number(counter), get_fib_number(counter+1)
    if a*b >= prod:
      flag = False
    counter += 1
  return [a, b, a*b == prod]


from TestFunction import Test
test = Test(None)   
test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])
