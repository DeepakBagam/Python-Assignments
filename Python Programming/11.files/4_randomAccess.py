f = open("hello.txt", "w")
f.write("My Bonnie lies over the ocean.")
f.close()
f = open("hello.txt", "r")
print(f.seekable())