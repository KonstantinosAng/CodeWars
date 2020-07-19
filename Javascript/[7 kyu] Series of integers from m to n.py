# see https://www.codewars.com/kata/5841f680c5c9b092950001ae/solutions/python

def generate_integers(m, n): 
    return [i for i in range(m , n+1)]

print(generate_integers(2, 5) == [2, 3, 4, 5])