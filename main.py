"""
import matplotlib.pyplot as plt
fruits = ['Mango', 'Grapes', 'Apple']
for fruit in fruits:
    print("Current fruit:", fruit)
print("good bye")


num = int(input("Number:"))
factorial = 1
if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num + 1):
     print(i)
     factorial = factorial*i
print(factorial)
"""
print("Welcome to Anand World Bank ATM")
restart = ("y")
chances = 3
balance = 650000
while chances >= 0:
    pin = int(input('please enter your 4 digit pin:'))
    if pin == (9618):
        print('hello ALUVALA ANAND\n')
        while restart not in ('n', 'NO','no','N'):
            print('Press 1 for your balance\n')
            print('Press 2 to make a Withdrawl\n')
            print('press 3 to pay in\n')
            print('press 4 to return card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('your Balance Available is:', balance, '\n')
                restart = input('would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print("thank you")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('how much would you like to withdraw?'))
                if withdrawl in [1000, 5000,10000,20000,50000,100000]:
                    balance = balance-withdrawl
                    print('\nyour balance is now available is :', balance)
                    restart = input('would you like to go back?')
                    if restart in ('n', 'NO','no','N'):
                        print('thank you')
                        break
                elif withdrawl:= [1000, 5000,10000,20000,50000,100000]:
                    print('INVAILD AMOUNT,Please re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please enter desired amount:'))
            elif option == 3:
                pay_in = float(input('Please Enter Desired amount:'))
                balance =balance + pay_in
                print('\nyour balance is now available', balance)
                restart = input('would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('thank you')
                    break
            elif option == 4:
                print('please wait whilst your card is returned....\n')
                print('thank you for your service')
                break
            else:
                print('please enter a correct number: \n')
                restart =('y')
    elif pin != ('9618'):
        print('incorrect password')
        chances = chances - 1
        if chances == 0:
            print('\n No more tries')
            break














