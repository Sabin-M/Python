print("welcome to Atm")
bal=0
user_pin=1234
pin=int(input("enter the pin"))
if(pin==user_pin):
    while True:
        print("\n ****Menu****\n 1.Balance \n 2.Deposit \n 3.Withdraw \n 4.Cancel \n")
        choice=int(input("enter your option:"))
        if(choice==1):
            print("your current balance is:₹",bal)
        elif(choice==2):
            dep=int(input("enter the amount to deposit:"))
            bal+=dep
            print("Your current balance is:₹ ",bal)
        elif(choice==3):
            withdraw = int(input("enter the amount to withdraw:"))
            bal-=withdraw
            print("Your current balance is:₹ ",bal)
        elif(choice==4):
            print("Thank you have a nice day")
            break
        else:
            print("invalid choice")
else:
    print("Invalid pin...please try again")
            
               
    
