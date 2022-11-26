class Test:

  def m1(self):
    self.student=str("deepak")
    print(self.student)

  def m1(self, roll):
    self.roll=int(roll)
    print('The roll number of student is',self.roll)

 


t = Test()

t.m1(10)
