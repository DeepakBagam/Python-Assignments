#Handle the Arithmetic exception using try-catch block
num = int(input("enter the number"))

try:
  print(num / 0)
except:
  print("number not divisible by zero")
