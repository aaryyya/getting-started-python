
# age=12
# if(age>=18):
#     print("vote")
# elif(age<18):
#     print("cant")
# else:
#     print("okay")

# light=input("Enter Traffic Color:")
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("watch and go")
# else:
#     print("invalid colour")


# marks=float(input("Enter Marks here: "))
# if(marks>=90):
#     print("A")
# elif(marks>=80 and marks<90):
#     print("B")
# elif(marks>=70 and marks<80):
#     print("B")
# else:
#     print("D")
#     print("Try Harder and dont fail")


# #Sinlge Line Conditional Statements
# #var=val1 if(condition)else val2
# food=input("food: ")
# eat="Yes" if food =="cake" else "no"
# print(eat)

# food=input("food: ")
# print("sweet") if food== "cake" or food== "jalebi" else print("not sweet")

# age =int(input("age:"))
# vote=("yes","no")[age<=18] #first value is for when the statement is false and secong for if it is true
# print(vote)

# sal=float(input("salary:"))
# tax=sal*(0.1,0.2)[sal<=5000]
# print(tax)

a,b=5,2
print("Arithmetic Operators")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#modulo or remainder
print(a**b)#a^b

print("Relational Operators")
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

print("Logical Operators")
val1=True
val2=False
print("AND Operator: ",val1 and val2)
print("OR Operator: ",val1 or val2)

print("OR operator:",(a==b)or(a>b))