#Write a Python program to implement a class named BankAccount with the following requirements:
#The class should contain two instance variables:
#Name (Account holder name)
#Amount (Account balance)
#The class should contain one class variable:
#ROI (Rate of Interest), initialized to 10.5
#Define a constructor (init) that accepts Name and initial Amount.
#Implement the following instance methods:
#Display()-displays account holder name and current balance
#Deposit() accepts an amount from the user and adds it to balance
#Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
#CalculateInterest()-calculates and returns interest using formula: Interest=(Amount * ROI) / 100
#Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        
        self.Name = Name
        self.Amount = Amount

    def Display(self):

        print(f"Account Holder name is :{self.Name}")
        print(f"Current balance is :{self.Amount}")

    def Deposit(self):
        Add = int(input("Enter Deposite amount :"))
        Balance = self.Amount + Add
        print("Balance is :",Balance)

    def Withdraw(self):
        Sub = int(input("Enter Withdraw amount :"))

        if self.Amount > Sub:
            Balance = self.Amount - Sub
            print("Remaining amount is :",Balance)

        else:
            print("Insufficient Balance")

    def CalculateInterest(self):

        Interest=(self.Amount * BankAccount.ROI) / 100
        print("Interest is :",Interest)
    
obj1 = BankAccount("Sam",100000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()


  