
print('Welcome to sindhu bankers')
chances = 3
balance = 23876
while chances > 0:
    pin = int(input("Enter 4 digit pin number "))
    if pin != 1234:
        print('Incorrect PIN')
        chances = chances - 1
        if chances == 0:
            print ('No more tries')

    elif (pin == 1234):
        print('PIN is correct\n')
        print("Press 1 for balance\n")
        print("Press 2 for withdrawl\n")
        print ("Press 3 to pay\n")
        print ("Press 4 to return card\n")
        option = int(input("Your option is:"))
        while option != 4:
            if option == 1:
                print("Balance= ", balance)
                option=0
            elif option == 2:
                withdrawl = int(input('How much you want to withdraw: '))
                balance = balance - withdrawl
                print('Your new balance: ', balance)
                option = 0
            elif option == 3:
                amount = int(input("How much to add? "))
                balance = balance + amount
                print('Your new balance: ', balance)
                option = 0
            else:

                print("Press 1 for balance\n")
                print("Press 2 for withdrawl\n")
                print ("Press 3 to pay\n")
                print ("Press 4 to return card\n")
                option = int(input("Your option is:"))
        break