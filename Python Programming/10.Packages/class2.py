class room():

  def __init__(self, branch, section):
    self.branch = branch
    self.section = section

  def details(self):
    print("the details are")
    print("Branch:", self.branch)
    print("Section:", self.section)
