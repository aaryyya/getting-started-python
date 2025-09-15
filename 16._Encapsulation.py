class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def resetpass(self):
        print(self.__acc_pass)
acc=Account("123","arya123")
print(acc.acc_no)
# print(acc.__acc_pass)
print(acc.resetpass())


class Person:
    __name="anonymous"
    def __hello(self):
        print("hello")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())
