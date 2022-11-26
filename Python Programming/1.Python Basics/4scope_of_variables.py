x=4 # Global Variable
y=5 # local Variable

def add():
  z=6 # local variable
  print(x+z)

add()
#print(z) It does not print because it not declaried globally if you want to print z use global keyword in function,