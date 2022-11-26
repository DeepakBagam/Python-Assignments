#pri access modifier
class student:

  def __init__(self, name, roll, branch):
    self._name = name
    self._roll = roll
    self._branch = branch

  def information(self):
    print("Name :", self._name)
    print("Roll :", self._roll)
    print("Branch :", self._branch)


class section(student):

  def __init__(self, name, roll, branch):
    super().__init__(name, roll, branch)

  def details(self, section):
    self._section = section
    print("The Student", self._name, "bearing", self._roll, "is in section",
          self._section)


myinf = section("Deepak", 201, "EEE")
myinf.details("A")
"""for importing the class from one package to the other pakage we can use the
FROM package name import class name"""