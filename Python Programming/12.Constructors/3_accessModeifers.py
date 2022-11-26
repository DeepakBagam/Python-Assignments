class Teacher:
  val1 = None
  _val2 = None
  __val3 = None

  def __init__(self, val1, val2, val3):
    self.val1 = val1
    self._val2 = val2
    self.__val3 = val3

  def dispPublicMembers(self):
    print("This is public member: ", self.val1)

  def _dispProtectedMembers(self):
    print("This is protected member: ", self._val2)

  def __dispPrivateMembers(self):
    print("This is private member: ", self.__val3)

  def accessPrivateMembers(self):
    self.__dispPrivateMembers()


class Child(Teacher):

  def __init__(self, val1, val2, val3):
    Teacher.__init__(self, val1, val2, val3)

  def accessProtectedMembers(self):
    self._dispProtectedMembers()


obj1 = Child("Hello", "Simon", 100000)
obj1.dispPublicMembers()
obj1.accessProtectedMembers()
obj1.accessPrivateMembers()
