class Employee:

  def sample(x):
    print('Inside static method', x)


Employee.sample = staticmethod(Employee.sample)
Employee.sample(10)
