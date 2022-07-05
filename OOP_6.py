#constructor in inheritance python
#inheritance in python
class A:#super class
    def __init__(self):
        print("hi")
    def rule1(self):
        print("rule 1")
    def rule2(self):
        print("rule 2")
        


class B(A):        #sub class(B inherit A)
    def __init__(self):
        print("B hi")
    def rule3(self):
        print("rule 3")
    def rule4(self):
        print("rule 4")
        
a1=B()