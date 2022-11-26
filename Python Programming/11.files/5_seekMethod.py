f = open("hello.txt", "r")
f.seek(2)

print(f.tell())
 
print(f.readline())
f.close()