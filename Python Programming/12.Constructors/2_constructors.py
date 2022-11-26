class Car:

  def __init__(self, model, make):
    self.name = "audi"  #default constructor
    self.model = model
    self.make = make

  def description(self):
    print("", self.name, "", self.model, "", self.make)

  def driver(self, drivername):
    self.drivername = drivername
    print("The", self.model, "car driver is", self.drivername)


class electric(Car):

  def __init__(self, model, make):
    super().__init__(model, make)

  def details(self):
    print("", self.name, "", self.model, "", self.make)


mycar = electric("audi5g", 2005)
mycar.details()
