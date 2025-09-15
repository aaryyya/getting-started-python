class Student:
    name="Channing"
    college="ameowining"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome stud,",self.name)

    def get_marks(self):
        return self.marks

    def hi():
        print("hi")
s1= Student("Siya",19)
s1.welcome()
# s1.hi()
print(Student.name)
print(s1.name)
print(s1.get_marks())



#     fullname="queen"
#     def __init__(self,fullname):
#         # print(self)
#         # print("Adding Stud")
#     # name="karn"
#         self.name=fullname

# # s1=Student("crinen")
# s1=Student("Arya")
# print(Student.fullname)
# # s2=Student("krik")
# # print()
# s2=Student("krik")
# print(s2.college,s2.name)
# print(Student.college,s2.name)

# # s2=Student()
# print(s2.name)

# class Car:
#     color="blue"
#     brand="mercedes"

# car1=Car()
# print(car1.color)
# print(car1.brand)