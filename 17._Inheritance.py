# Single Inheritance

class Car:
    def __init__(self,type):
        self.type=type
    color="green"
    @staticmethod
    def start():
        print("car started parent")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
        #self.type=type here whichuu have ceatef is of toyota car class and not parent class
        super().__init__(type)
        super().start()
car1=ToyotaCar("fortuner","toyota")
# car2=ToyotaCar("priss")

print(car1.name)
print(car1.start())
print(car1.color)

#Multilevel INheritance
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car3=Fortuner("disel")
car3.start()


#MUltiple Inheritance
class A:
    varA="Welcome class A here"
class B:
    varB="Welcome class B here"
class C(A,B):
    varC="Welcome class C here"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)




# missed commit restoration//
# //second#123commit
#//commit //