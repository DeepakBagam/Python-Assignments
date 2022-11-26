#Write a program to generate FileNotFoundException
try:
  f=open("hello.txt","r")
  print("file opend")
except:
  print("file not found")
  