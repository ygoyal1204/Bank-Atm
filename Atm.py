class ATM:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def checkBalance(self):
        print("Your balance is Rs 5000")

    def withdrawl(self, amount):
        if amount > 5000:
            print("Money insufficent")

        else:
            balance = 5000 - amount
            print("You have withdrawn ", amount, ". Your remaining balance is ", balance)

def main():
    cardNumber = input("Enter your card number: ")
    pinNumber = input("Enter your pin: ")
    newUser = ATM(cardNumber, pinNumber)

    print("What do you want to do? Choose your activity.")
    print("1. Balance Enquiry")
    print("2. Money Withdrawl")
    
    activity = int(input("Enter your activity number: "))

    if activity == 1:
        newUser.checkBalance()

    elif activity==2:
        amount = int(input("Enter the amoutn you want to withdraw: "))
        newUser.withdrawl(amount)

    else:
        print("Enter a valid number.")

main()