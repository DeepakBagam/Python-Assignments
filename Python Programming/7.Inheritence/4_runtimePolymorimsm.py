class Car:  #Parent Class or class A

  def __init__(self, name, model, make):
    self.name = name
    self.model = model
    self.make = make

  def description(self):
    print("", self.name, "", self.model, "", self.make)

  def driver(self, drivername):
    self.drivername = drivername
    print("The", self.model, "car driver is", self.drivername)

  def fuel(self, fuel):  #common method
    self.fuel = fuel
    print("the fuel for", self.name, "&", self.model, "car is", self.fuel)


class ElectricCar(Car):  #child calss1 or class B

  def __init__(self, name, model, make):
    super().__init__(name, model, make)
    self.battery_size = 75

  def battery(self):
    print("the battery size is", self.battery_size, "in the year", self.make)

  def speed(self, speed):
    self.speed = speed
    print("the speed of Electric car", self.speed, "of model", self.model)

  def fuel(self, fuel):
    self.fuel = fuel
    print("the fuel for Electric ", self.name, "&", self.model, "car is",
          self.fuel)


class toyCar(ElectricCar):  #child class 2 or class B

  def __init__(self, name, model, make):
    super().__init__(name, model, make)

  def size(self, size):
    self.size = size
    print("the size of toy car is", self.size, "of model", self.model)

  def price(self, price):
    self.price = price
    print("the price of toy car is", self.price, "of model", self.model)

  def fuel(self):
    print("No fuel required for toy car")


#calling through methods by instance
my_car = Car("Benz", "d5", 2012)
print(my_car.name)
print(my_car.model)
print(my_car.make)
my_car.description()
my_car.driver("Deepak")
my_car.fuel("petrol")

my_car1 = ElectricCar("Jaguar", "A1", 2020)
print(len(my_car1.name))  # runtime Polymorizm
print(my_car1.model)
print(my_car1.make)
my_car1.description()
my_car1.driver("Ramu")
my_car1.battery()
my_car1.speed(200)
my_car1.fuel("petrol")

my_car2 = toyCar("Audi", "a4", 2004)
print(my_car2.name)
print(len(my_car2.model))  # runtime Polymorizm
print(my_car2.make)
my_car2.description()
my_car2.driver("Somu")
my_car2.battery()
my_car2.speed(2)
my_car2.price(10)
my_car2.size(20)
my_car2.fuel()
