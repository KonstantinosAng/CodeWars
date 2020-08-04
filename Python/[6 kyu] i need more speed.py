# see https://www.codewars.com/kata/55de9c184bb732a87f000055/solutions

from TestFunction import Test

def reverse(seq): 
    for i in range(len(seq)>>1):
        seq[i],seq[-i-1] = seq[-i-1],seq[i]

test = Test(None)
seq = [1,2,3,4,5]
reverse(seq)
test.assert_equals([5,4,3,2,1], seq)

seq = ['?','you','are','how','world','hello']
reverse(seq)
test.assert_equals(['hello','world','how','are','you','?'], seq)

seq = [{'b':2},{'a':1}]
reverse(seq)
test.assert_equals([{'a':1},{'b':2}], seq)
