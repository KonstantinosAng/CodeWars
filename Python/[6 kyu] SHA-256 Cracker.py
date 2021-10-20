# see https://www.codewars.com/kata/587f0abdd8730aafd4000035/train/python

from itertools import permutations
import hashlib

def sha256_cracker(hash, chars):
  for permutation in ["".join(permutation) for permutation in list(permutations(chars))]:
    encodedPermutation = permutation.encode()
    hashedPermutation = hashlib.sha256(encodedPermutation)
    if hashedPermutation.hexdigest() == hash: return permutation
  return None    
  

from TestFunction import Test
test = Test(None)

test.assert_equals(sha256_cracker('b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae', 'deGioOstu'), 'GoOutside')
test.assert_equals(sha256_cracker('f58262c8005bb64b8f99ec6083faf050c502d099d9929ae37ffed2fe1bb954fb', 'abc'), None)