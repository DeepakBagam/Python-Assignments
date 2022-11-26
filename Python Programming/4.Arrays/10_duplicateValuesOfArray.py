lst=[1,2,2,6,8,4,6]

for i in range(0,len(lst)):
  for j in range(i+1,len(lst)):
    if (lst[i]==lst[j]):
      print(j)
  
