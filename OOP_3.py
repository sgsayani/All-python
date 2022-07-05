#types of method

class student:
    
    Univ="Jis university"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self): #instanse method
        return(self.m1+self.m2+self.m3)/3
   
    def get_m1(self):#accessor methods
        return self.m1
    
    def set_m1(self,value):#mutetor method
        self.m1=value    
     
    #class method
    @classmethod   #decorator (info as a cls method )
    def info(cls):
        return cls.Univ
     
     
    #static method
    @staticmethod
    def info():
        print("this is student class")   
        
s1=student(10, 20, 30)
s2=student(20, 30, 40)

print(s1.avg())
print(s2.avg())
print(student.info())
student.info()
