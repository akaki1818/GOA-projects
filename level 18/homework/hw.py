#bank
print("1. balance")
print("2. transfer money")
print("3.deposit to your account")
print("4.currency converter")
number = int(input("number:"))


if number == 1:
    print("you have 100 gel")

elif number == 2:
    account_number = int(input("enter account number"))
    amount = int(input("Enter how uch do you want to transfer"))
    print (int(amount + 10))

elif number == 3:
    input("enter password")
    amountt = int(input("enter amount"))

elif number ==  4:
    print ("1.usd to gel")
    print("1.gel to usd")
    select = int(input("choose which currency to transfer"))
    if select == 1:
        amounttt = int(input("enter amount"))
        print(amounttt * 2.69)
    if select == 2:
        amounts = int(input("enter amount"))
        print(amounts * 0.37)
