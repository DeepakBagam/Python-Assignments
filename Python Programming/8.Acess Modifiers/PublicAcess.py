#public access modifier
class student:

  def __init__(self, name, roll, branch):
    self.name = name
    self.roll = roll
    self.branch = branch

  def information(self):
    print("Name :", self.name)
    print("Roll :", self.roll)
    print("Branch :", self.branch)


myinf = student("Deepak", 201, "EEE")
myinf.information()