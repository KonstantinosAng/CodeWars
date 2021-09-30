# see https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def sort_equals(arr, position):
  start = position
  end = position
  while arr[start][1] == arr[end][1]:
    end += 1
    if end == len(arr): break
  end = end if end < len(arr) else len(arr) + 1
  temp_array = sorted([x for x in arr[start:end]], key=lambda x: x[0])
  retArray = arr[:start] + temp_array + arr[end:]
  return retArray


def order_weight(strng):
  hashMap = [[key, sum(int(x) for x in key)] for key in strng.strip().split(" ") if key != ""]
  retArray = sorted([x for x in hashMap], key=lambda x: x[1])
  position = 0
  while position < len(retArray) - 1:
    if retArray[position][1] == retArray[position+1][1]:
      retArray = sort_equals(retArray, position)
    position +=1
  return " ".join(x[0] for x in retArray)


from TestFunction import Test
test = Test(None)   
test.describe("Weight for weight")
test.it("basic tests")
test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
test.assert_equals(order_weight("265454 217839 79993 276598"), "265454 217839 276598 79993")
test.assert_equals(order_weight(""), "")
test.assert_equals(order_weight(" 376909 486466 387699   97 36 146"), "36 146 97 376909 486466 387699")
test.assert_equals(order_weight("87138 56819 345585  383548 55859 108968"), "87138 56819 345585 383548 108968 55859")