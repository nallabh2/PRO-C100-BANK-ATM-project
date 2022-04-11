class Atm:
  __init__(self,cardNum,pinNum,initialBalance):
    self.cardNum=cardNum
    self.pinNum=pinNum
    self.balance=initialBalance
    
  def CashWithdrawl(self,amount,card,pin):
  	print(amount+" has been withdrawn")
    self.balance-=amount
    
  def BalanceEnquiry(self,card,pin):
    print("your balance is "+self.balance)
