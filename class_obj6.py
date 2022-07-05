class account:
    def __init__(self,money):
        self.money=money
    def deposit(self,ex_money):
        self.money+=ex_money
    def withdrawn(self,with_money):
        self.money-=with_money
        print(f"the withdrawn money is {with_money} and the money have {self.money}")
ac=account(5000)
ac.withdrawn(200)
ac.deposit(500)
ac.withdrawn(1000)