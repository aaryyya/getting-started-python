collection={1,2,3,2,"World","World","Meows"}
print(collection)#no repetion of elements in printed sets
print(type(collection))
print(len(collection))
null_set_syntax=set()
print(type(null_set_syntax))

collection.add("my universe")
print(collection)
collection.add((1,2,3,4,5))
collection.remove(1)
print(collection)
collection.pop()
print(collection)
collection.clear()
print(collection)
collection.add((1,2,3,4,5))
print(collection)

set1={1,2,3}
set2={3,4,5}

set3=set1.union(set2)
print(set3)
set3=set1.intersection(set2)
print(set3)


subjects={"py","j","c++","py","js","py","j","c++","c",}
lenny=(len(subjects))
print(lenny)


marks={}
x=input("Enter marks of Physics: ")
marks.update({"phy":x})
x=input("Enter marks of Maths: ")
marks.update({"Maths":x})
x=input("Enter marks of Chem: ")
marks.update({"chem":x})
print(marks)