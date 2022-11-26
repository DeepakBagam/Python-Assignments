lst = [1, 2, 2, 6, 6, 4, 6]
list = []
for i in lst:
  if i not in list:
    list.append(i)
print(list)
