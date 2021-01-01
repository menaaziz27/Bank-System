import csv


def Reading_CSV():
    with open('sample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_reader:
            list_of_rows.append(row)
        return list_of_rows


# Validate user and get user data if the account number valid
# if it's not Valid return False
def Write_updated_data(listOfData):
    writer_obj = open('sample.csv', 'w', newline='')
    csv_writer = csv.writer(writer_obj)
    csv_writer.writerows(listOfData)
    writer_obj.close()


# ---Global Variables---
List_of_allData = Reading_CSV()


def get_client_data(account_num):

    for index, row in enumerate(List_of_allData):
        if(account_num in row):
            return index, row

    return False

def starting_welcome():
    print('Weclome!')


def welcome(name):
    print(f'Welcome {name}')


# Show user current balane
def ShowBalance(user_row):
    print(user_row[2])


# user deposite process:
def deposite(user_row_index, user_row, amount):

    updated_user_salary = float(user_row[2]) + amount
    user_row[2] = updated_user_salary
    List_of_allData[user_row_index] = user_row

    # update the data in the csv file
    Write_updated_data(List_of_allData)

    print('deposite process is done successfully!')


# TODO handle errors and user input
def withdrawal(user_row_index, user_row, withdraw_amount):

    updated_user_salary = float(user_row[2]) - withdraw_amount
    user_row[2] = updated_user_salary
    List_of_allData[user_row_index] = user_row
    Write_updated_data(List_of_allData)
    print('Withdraw process is done successfully!')


def run():

    """ Starting the system """

    while(True):
        try:
            accountNumber = input("Enter your bank account number ?\n")
            # the user row in csv
            user_row_index, valid_user = get_client_data(accountNumber)
            if(valid_user):
                break
        except Exception as e:
            print('invalid account number')
            continue

    # if the user account exists ..
    if(valid_user):
        # print(valid_user)
        username = valid_user[1]
        # print(username)
        isRunning = True

        # welcome and show him the menu show him the menu
        welcome(username)

        while(isRunning):
            print('1) Show current balance.')
            print('2) Make a deposite.')
            print('3) Make a withdrawal.')
            print('4) Exit.')
            choice = input()
            if(choice == '1'):
                ShowBalance(valid_user)
            elif choice == '2':
                while True:
                    try:
                        amount = int(input("Enter Amount Number: "))
                        if(amount):
                            break
                    except:
                        print('Strings not valid. try with a number')
                        
                # make sure that the user input is a positive number
                if (amount > 0):
                    deposite(user_row_index, valid_user, amount)
                else:
                    print('amount must be a positive number')
                    continue
            elif choice == '3':
                # TODO check if the user enters a string
                #! notice
                try:
                    withdraw_amount = int(
                        input("Enter the amount you want to withdraw: "))
                except:
                    print('Strings are not a valid input')
                    continue
                # make sure that the user input is a positive number
                if (withdraw_amount > 0):
                    if(float(valid_user[2]) < withdraw_amount):
                        print(
                            "You cannot withdraw amount that's larger than the existing one")
                        continue
                    withdrawal(user_row_index, valid_user, withdraw_amount)
                elif (withdraw_amount < 0):
                    print('amount must be a positive number')
                    continue
                else:
                    print('Strings are not a valid input')
            elif choice == '4':
                print(f"GoodBye, {valid_user[1]}")
                isRunning = False
            else:
                print('Unexpected input .. the must input digits e.g 1,2,3,4')
        # else block to handle user input
    else:
        # print him an error and let him try again
        print('Bank account number is invalid.\nTry again!')
        run()


starting_welcome()
run()
