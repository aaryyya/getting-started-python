class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hi")
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi,",self.name,"your avg score:",sum/3)
s1=Student("Tony Stark",[99,98,78])
s1.get_avg()
s1.name="namor"
s1.get_avg()
s1.hello()

    