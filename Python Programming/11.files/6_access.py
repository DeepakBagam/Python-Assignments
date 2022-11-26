
import os
import sys

path1 = os.access("hello.txt", os.F_OK)
print("Exists the path:", path1)

path2 = os.access("hello.txt", os.R_OK)
print("Access to read the file:", path2)

path3 = os.access("hello.txt", os.W_OK)
print("Access to write the file:", path3)

path4 = os.access("hello.txt", os.X_OK)
print("Check if path can be executed:", path4)
