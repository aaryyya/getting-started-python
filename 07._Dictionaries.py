info = {
    "key":"value",
    "name" : "arya",
    "learning":"coding",
    "isAdult":True,
    "marks":94,
    "subjects":["MAths","Sci","English"],
    "topics":("dic","set")

}
print(info)
print(info["learning"])

print(info["name"])
print(info["marks"])
info["name"]="Arya"

info["surname"]="Patil"
print(info)


null_dict={

}
print(null_dict)


student={
    "name":"rahul",
    "subjects":{
        "phy":91,
        "chem":56,
        "math":41,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])
keyed1=student.keys()
print(keyed1)
keyed=student["subjects"].keys()
print(keyed)
keyed2=student.values()
print(keyed2)
keyed3=student.items()
print(keyed3)
keyed4=student.get("name")
keyed5=student.get("subjects")
print(keyed4)
print(keyed5)
keyed6=student.update()

