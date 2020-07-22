# see https://www.codewars.com/kata/558fa34727c2d274c10000ae/solutions/python

from TestFunction import Test

def scrabble_score(st): 
    values = {"aeioulnrst": 1, "dg": 2, "bcmp": 3, "fhvwy": 4, "k": 5, "jx": 8, "qz": 10}
    score = 0
    for letter in st:
      for key, value in values.items():
        if letter.lower() in key:
          score += value
    return score


Test(0).assert_result(scrabble_score(""))
Test(1).assert_result(scrabble_score('a'))
Test(6).assert_result(scrabble_score("street"))
Test(6).assert_result(scrabble_score("STREET"))
Test(1).assert_result(scrabble_score(' a'))
Test(6).assert_result(scrabble_score("st re et"))