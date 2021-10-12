# see https://www.codewars.com/kata/5bc7bb444be9774f100000c3/train/python


class VersionManager:
  def __init__(self, version="0.0.1"):
    if version == "": self.currentVersion = "0.0.1"
    else:
      tempVersion = version.split(".")
      if len(tempVersion) < 3:
        while len(tempVersion) < 3:
          tempVersion.append("0")
      elif len(tempVersion) > 3: 
        tempVersion = tempVersion[:3]
      else: tempVersion = tempVersion
      self.currentVersion = ".".join(tempVersion)
    if False in [True if x.isdigit() else False for x in self.currentVersion.split(".")]: raise Exception("Error occured while parsing version!")
    self.previousVersion = []

  def major(self):
    self.previousVersion.append(self.currentVersion)
    self.currentVersion = ".".join([str(int(self.currentVersion.split(".")[0]) + 1), '0', '0'])
    return self

  def minor(self):
    self.previousVersion.append(self.currentVersion)
    self.currentVersion = ".".join([self.currentVersion.split(".")[0], str(int(self.currentVersion.split(".")[1]) + 1), '0'])
    return self

  def patch(self):
    self.previousVersion.append(self.currentVersion)
    self.currentVersion = ".".join([self.currentVersion.split(".")[0], self.currentVersion.split(".")[1], str(int(self.currentVersion.split(".")[2]) + 1)])
    return self

  def release(self):
    return self.currentVersion

  def rollback(self):
    if len(self.previousVersion) > 0: self.currentVersion = self.previousVersion.pop(-1)
    else: raise Exception("Cannot rollback!")
    return self

from TestFunction import Test
test = Test(None)

test.describe("Sample tests")

test.it("Initialization tests")
test.assert_equals(VersionManager().release(), "0.0.1", "Default initial version")
test.assert_equals(VersionManager("").release(), "0.0.1", "Default initial version")
test.assert_equals(VersionManager("1.2.3").release(), "1.2.3", "No version changes")
test.assert_equals(VersionManager("1.2.3.4").release(), "1.2.3", "No version changes")
test.assert_equals(VersionManager("1.2.3.d").release(), "1.2.3", "No version changes")
test.assert_equals(VersionManager("1").release(), "1.0.0", "Default minor version is 0")
test.assert_equals(VersionManager("1.1").release(), "1.1.0", "Default patch is 0")

# test.it("Major releases tests")
test.assert_equals(VersionManager().major().release(), "1.0.0")
test.assert_equals(VersionManager("1.2.3").major().release(), "2.0.0")
test.assert_equals(VersionManager("1.2.3").major().major().release(), "3.0.0")

# test.it("Minor releases tests")
test.assert_equals(VersionManager().minor().release(), "0.1.0")
test.assert_equals(VersionManager("1.2.3").minor().release(), "1.3.0")
test.assert_equals(VersionManager("1").minor().release(), "1.1.0")
test.assert_equals(VersionManager("4").minor().minor().release(), "4.2.0")

# test.it("Patch releases tests")
test.assert_equals(VersionManager().patch().release(), "0.0.2")
test.assert_equals(VersionManager("1.2.3").patch().release(), "1.2.4")
test.assert_equals(VersionManager("4").patch().patch().release(), "4.0.2")

# test.it("Rollbacks tests")
test.assert_equals(VersionManager().major().rollback().release(), "0.0.1")
test.assert_equals(VersionManager().minor().rollback().release(), "0.0.1")
test.assert_equals(VersionManager().patch().rollback().release(), "0.0.1")
test.assert_equals(VersionManager().major().patch().rollback().release(), "1.0.0")
test.assert_equals(VersionManager().major().patch().rollback().major().rollback().release(), "1.0.0")

test.it("Seperated calls")
m = VersionManager("1.2.3")
m.major()
m.minor()
test.assert_equals(m.release(), "2.1.0")

test.it("Exception calls")
try:
    VersionManager("a.b.c")
    test.fail("Should throw when initial version cannot be parsed")
except Exception as e:
    test.assert_equals(str(e), "Error occurred while parsing version!")
    
try:
    VersionManager().rollback()
    test.fail("Should throw when cannot rollback")
except Exception as e:
    test.assert_equals(str(e), "Cannot rollback!")