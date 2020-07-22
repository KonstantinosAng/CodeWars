# see https://www.codewars.com/kata/55ed875819ae85ca8b00005c/solutions/pythons

def multiply_and_filter(seq, multiplier): 
    return [i*multiplier for i in seq if type(i) == int or type(i) == float]


print(multiply_and_filter([1,2,3,4], 1.5) == [1.5, 3, 4.5, 6])
print(multiply_and_filter([1,2,3], 0) == [0, 0, 0])
print(multiply_and_filter([0,0,0], 2) == [0, 0, 0])
print(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, []], 3) == [3,7.5,30])
print(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, [], True, False], 3) == [3,7.5,30])
