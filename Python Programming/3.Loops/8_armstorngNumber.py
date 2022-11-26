num = int(input("Enter a number: "))
count = 0
sum = 0
temp = tnum = num

while temp % 10 != 0:
  count += 1
  temp = temp // 10
while num != 0:
  digit = num % 10
  sum = sum + (digit**count)
  num = num // 10

if (tnum == sum):
  print("", tnum, "is Armstrong Number")
else:
  print("", tnum, "is not a armstrong number")
