# see https://www.codewars.com/kata/59d0ee709f0cbcf65400003b/train/python

from collections import defaultdict
import re

PATTERN = re.compile(r'(.+?), (.+?), (.+?(?= [A-Z]{2})) ([A-Z]{2})')
STATES = {"CA": "California",
          "MA": "Massachusetts",
          "OK": "Oklahoma",
          "PA": "Pennsylvania",
          "VA": "Virginia",
          "AZ": "Arizona",
          "ID": "Idaho",
          "IN": "Indiana"}

def by_state(s):
  dct = defaultdict(list)
  for name,addrs,city,state in PATTERN.findall(s):
    dct[STATES[state]].append("..... {} {} {} {}".format(name, addrs, city, STATES[state]))
    
  return '\r\n '.join( "{}\r\n{}".format(state, '\r\n'.join(sorted(lst))) for state,lst in sorted(dct.items()) )


from TestFunction import Test
test = Test(None)

case0 = """John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Sal Carpenter, 73 6th Street, Boston MA"""

case1 = """John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
Terry Kalkas, 402 Lans Road, Beaver Falls PA
Eric Adams, 20 Post Road, Sudbury MA
Hubert Sims, 328A Brook Road, Roanoke MA
Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
Sal Carpenter, 73 6th Street, Boston MA"""

test.describe("by_state")
test.it("Basic tests")
answer = "Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n..... Sal Carpenter 73 6th Street Boston Massachusetts\r\n Virginia\r\n..... Alice Ford 22 East Broadway Richmond Virginia"
test.assert_equals(by_state(case0), answer)
answer = "California\r\n..... Amy Wilde 334 Bayshore Pkwy Mountain View California\r\n Massachusetts\r\n..... Eric Adams 20 Post Road Sudbury Massachusetts\r\n..... Hubert Sims 328A Brook Road Roanoke Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n..... Sal Carpenter 73 6th Street Boston Massachusetts\r\n Oklahoma\r\n..... Orville Thomas 11345 Oak Bridge Road Tulsa Oklahoma\r\n Pennsylvania\r\n..... Terry Kalkas 402 Lans Road Beaver Falls Pennsylvania\r\n Virginia\r\n..... Alice Ford 22 East Broadway Richmond Virginia"
test.assert_equals(by_state(case1), answer)