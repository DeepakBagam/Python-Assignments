x = int(input("Enter Number\n"))
y = int(input("Enter Number\n"))
z = int(input("Enter Number\n"))
if (x > y and x > z):
  print("The", x, "is Greater Than Others")
elif (y > z):
  print("The", y, "is Greater Than Others")
else:
  print("The", z, "is Greater Than Others")
