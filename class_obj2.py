#ass 11 prb 1
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avarage(self):
        self.m1=sum(self.marks)
        self.m1=self.m1//len(self.marks)
        print(self.m1)
    def show(self):
        print("the name is{} marks is {}".format(self.name,self.marks))

std = student('sayani',[60,40,50,78,54,45])
std.avarage()
std.show()  

            