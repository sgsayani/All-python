class circle:
    def __init__(self,redius):
        self.redius=redius
    def area(self):
        self.r = 3.14*self.redius*self.redius
        print("area is ",(self.r))
    def circum(self):
        self.c = 2 *3.14*self.redius
        print("circumference is ",(self.c))
p1=circle(5)
p1.area()
p1.circum()