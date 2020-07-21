# see https://www.codewars.com/kata/59f7fc109f0e86d705000043/solutions/python

def divisible_by_three(st): 
    return True if sum([int(x) for x in st])%3 == 0 else False

print(divisible_by_three('123') == True)
print(divisible_by_three('19254') == True)
print(divisible_by_three('88') == False)
print(divisible_by_three('1') == False)

