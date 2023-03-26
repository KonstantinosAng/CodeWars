# see https://www.codewars.com/kata/5269452810342858ec000951/train/python

from TestFunction import Test

def is_valid_coordinates(coordinates):
    if "," not in coordinates: return False
    if len(coordinates.split(",")) > 2: return False
    if "e" in coordinates: return False
    latitude, longitude = coordinates.split(",")
    try:
      parsed_latitude, parsed_longitude = float(latitude), float(longitude)
      if parsed_latitude > 90 or parsed_latitude < -90: return False
      if parsed_longitude > 180 or parsed_longitude < -180: return False
      return True
    except ValueError:
        return False


test = Test(None)
test.describe("Example Test Cases")

test.it("should return true for valid coordinates")
valid_coordinates = [
    "-23, 25",
    "4, -3",
    "24.53525235, 23.45235",
    "04, -23.234235",
    "43.91343345, 143"
]

for coordinate in valid_coordinates:
    test.expect(is_valid_coordinates(coordinate), "%s validation failed." % coordinate)
    
test.it("should return false for invalid coordinates")
invalid_coordinates = [
    "23.234, - 23.4234",
    "2342.43536, 34.324236",
    "N23.43345, E32.6457",
    "99.234, 12.324",
    "6.325624, 43.34345.345",
    "0, 1,2",
    "0.342q0832, 1.2324",
    "23.245, 1e1"
]

for coordinate in invalid_coordinates:
    test.expect(not is_valid_coordinates(coordinate), "%s validation failed." % coordinate)
