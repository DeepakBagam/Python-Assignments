import abc
from abc import ABC, abstractmethod


class parent(ABC):

  @abc.abstractmethod
  def __init__(self, name, roll):
    self.name = name
    self.roll = roll

  def description(self):
    print("the name os student is", self.name)

  def rank(self):
    pass


class child(parent):

  def __init__(self, name, roll):
    super().__init__(name, roll)

  def rank(self, grade):
    self.grade = grade
    print("", self.grade)


r = child("deepak", 205)
r.rank(2)
