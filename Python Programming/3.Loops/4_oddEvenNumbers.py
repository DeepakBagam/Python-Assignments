x = int(input("Enter Number\n"))
if (x % 2 == 0):
  print("The number is even ")
else:
  print("The number is odd")

even = []
odd = []
for i in range(x):
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)

print("the Even number from 0 to", (x - 1), "is")
print(even)
print("the odd number from 0 to", (x - 1), "is")
print(odd)