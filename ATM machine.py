#create a machine that a words discounts to users depending on their
# withdrawal amount and display the total amount inclusive of the discounts.
#withdrawal above 10,000 award a discount of 15%,
#withdrawal above 5000 give give a discount of of 10% and lastly a
#withdrawal above 2000 give a discount of 5%

def calculateDiscount(withdrawalAmount):
    if withdrawalAmount > 10000:
        discount= 0.15
    elif withdrawalAmount > 5000:
        discount = 0.10
    elif withdrawalAmount > 2000:
        discount = 0.05
    else:
        discount = 0.00
    return discount
def withdrawalAmount():
    withdrawalAmount=float(input("Enter amount you want to withdraw: "))
    discount=calculateDiscount(withdrawalAmount)
    dicountedAmount=withdrawalAmount-(withdrawalAmount*discount)
    print("Withdrawal amount is: ",dicountedAmount)
if __name__== "__main__":
    withdrawalAmount()