class number:
    def __init__(self,num):
        self.num = num
    def large(self):
        a = max(self.num)
        return a
    
m= list(map(int, input().rstrip().split()))
lg =  number(m)
print(lg.large())