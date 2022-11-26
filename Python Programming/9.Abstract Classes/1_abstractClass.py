from abc import ABC, abstractmethod


#Abstract Class with abstract method
class student(ABC):

  @abstractmethod
  def animal(self):
    print("It's all about animals")

  def duck(self):
    print("It's a bird")

  def cat(self):
    print("It drinks milk")


#Abstract Class with non-abstract method
class student1(ABC):

  def animal1(self):
    print("It's all about animals")

  def duck1(self):
    print("It's a bird")

  def cat1(self):
    print("It drinks milk")


s = student1()
s.duck1()
