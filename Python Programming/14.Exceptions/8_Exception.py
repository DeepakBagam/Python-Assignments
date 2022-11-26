#Write a program to generate Arithmetic Exception

try:
    k = 5//0  
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")
 
