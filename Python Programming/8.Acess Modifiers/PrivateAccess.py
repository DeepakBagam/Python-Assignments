#private access modifier
class student:

  def __init__(self, name, roll, branch):
    self.__name = name
    self.__roll = roll
    self.__branch = branch

  def information(self):
    print("Name :", self.__name)
    print("Roll :", self.__roll)
    print("Branch :", self.__branch)


#private methods are not inherited
"""class section():
  def __init__(self,name,roll,branch):
    super().__init__(name,roll,branch)
    self.__section='A'
  def details(self):
    print("The Student",self.__name,"bearing",self.__roll,"is in section",self.__section)"""

myinf = student("Deepak", 201, "EEE")
myinf.information()