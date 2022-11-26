list = [1, 3, 5, 6, 8, 9, 12, 45, 62, 9, 5, 45, 2, 65]
even = []
odd = []
for i in list:
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)
print("Even numbers in the list")
print(even)
print("odd numbers in the list")
print(odd)
