f = open("hello.txt", "w")
f.write("Welcome all")
f.close()

f = open("hello.txt")
print(f.read())
