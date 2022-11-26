dictionary={
 "deepak":201,
  "Ramu":202,
  "somu":203,
  "Ravan":204,
  "Ragav":205
}
#Adding Values
dictionary["Raju"]=206
print(dictionary)
#Acessing the values in dictionary
x=dictionary.values()
print(x)
y=dictionary.keys()
print(y)
print(dictionary.get("Ravan"))

#changing and updating
dictionary["raju"]=207
print(dictionary)
dictionary.update({"raju":206})
print(dictionary.items())

#Nested loop in dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print key and values
a=myfamily.values()
print(a)
b=myfamily.keys()
print(b)
#Remove a value from dictionary
print(myfamily.pop("child1"))
print(myfamily.items())