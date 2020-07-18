# see https://www.codewars.com/kata/563b662a59afc2b5120000c6/solutions/python

def nb_year(p0, percent, aug, p):
    years, population = 0, p0
    while population < p:
        years += 1
        population += population*percent/100 + aug
    return years
  
print(nb_year(1500, 5, 100, 5000) == 15)
print(nb_year(1500000, 2.5, 10000, 2000000) == 10)
print(nb_year(1500000, 0.25, 1000, 2000000) == 94)