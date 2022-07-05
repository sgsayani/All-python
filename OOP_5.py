#inheritance in python
class A:#super class
    def rule1(self):
        print("rule 1")
    def rule2(self):
        print("rule 2")
        


class B(A):        #sub class(B inherit A)
    def rule3(self):
        print("rule 3")
    def rule4(self):
        print("rule 4")


class C(B):
    def rule5(self):
        print("rule 5")
    def rule6(self):
        print("rule 6")

a1=A()
a1.rule1()
a1.rule2()


b1=B()
b1.rule3()
b1.rule4()


c1=C()
c1.rule1()