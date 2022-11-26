#Write a program with multiple catch blocks
def fun(a):
    if a < 4:

        b = a/(a-3)

    print("Value of b = ", b)
     
try:
    fun(3)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")