class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "Hello, %s. Your balance is $%s.2f" % (self.name, self.balance)
  def show_balance():
    print balance
  def deposit(self, amount):
    self.amount = amount
    amount = raw_input("What would you like to deposit?")
    if amount <= 0: 
      print "You can't deposit negative money!"
      return
    else:
      print "You are depositing $%s.2f" % (amount)
      balance += amount
      self.show_balance()
  def withdraw(self, amount):
    self.amount = amount
    amount = raw_input("How much would you like to withdraw?")
    if amount > balance: 
      print "You can't withdraw that much money!"
      return
    else: 
      print "You are withdrawing $%s.2f" % (amount)
      balance -= amount
      self.show_balance()
      
my_account = BankAccount("Aliesha")
my_account.deposit(2000)
