    def __init_(self,name):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome stud,",self.name)

    def get_marks(self):
        return self.marks

    s1=Student("Siya",19)
    s1.welcome()
    print(s1.get_marks())