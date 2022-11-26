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


mycar = Car("5g", 2004)
mycar.description()