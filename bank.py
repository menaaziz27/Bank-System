import csv


def Reading_CSV():
    with open('sample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print(csv_reader)
        list_of_rows = []
        for row in csv_reader:
            list_of_rows.append(row)
        return list_of_rows


# Validate user and get user data if the account number valid
# if it's not Valid return False
def Write_updated_data(listOfData):
    writer_obj = open('sample.csv', 'w')
    csv_writer = csv.writer(writer_obj)
    csv_writer.writerows(listOfData)
    writer_obj.close()


# ---Global Variables---
List_of_allData = Reading_CSV()


def get_client_data(account_num):

    for index, row in enumerate(List_of_allData):
        # print(row)
        if(account_num in row):
            # print('yes!')
            return index, row

    return False


def welcome():
    print("Welcome .. let me help you!")


# Show user current balane
# !works
def ShowBalance(user_row):
    print(user_row[2])
    # pass


# user deposite process:
# !works
def deposite(user_row_index, user_row, amount):
    # updated_user_salary
    updated_user_salary = float(user_row[2]) + amount
    user_row[2] = updated_user_salary
    # ShowBalance(user_row)
    List_of_allData[user_row_index] = user_row
    Write_updated_data(List_of_allData)
    print('deposite process is done successfully!')
    # print(updated_row)
    pass
    # user withdrawal

# TODO handle errors and user input


def withdrawal(user_row_index, user_row, withdraw_amount):

    # 12000 => 13000
    updated_user_salary = float(user_row[2]) - withdraw_amount
    user_row[2] = updated_user_salary
    # ShowBalance(user_row)
    List_of_allData[user_row_index] = user_row
    Write_updated_data(List_of_allData)
    print('Withdraw process is done successfully!')
    # print(List_of_allData)
    # pass


def run():
    """
    start the system
    """
    accountNumber = input("What's your account number ?\n")
    # check if the user input is actually a number
    # if(type(accountNumber) == str):
    #     print('Strings not valid. try with a number')
    #     return run()

    # the user row in csv
    user_row_index, valid_user = get_client_data(accountNumber)

    # if the user account exists ..
    if(valid_user):

        isRunning = True

        # welcome and show him the menu show him the menu
        welcome()

        while(isRunning):
            print('1) Show current balance.')
            print('2) Make a deposite.')
            print('3) Make a withdrawal.')
            print('4) Exit.')
            choice = input()
            if(choice == '1'):
                ShowBalance(valid_user)
            elif choice == '2':
                amount = int(input("Enter Amount Number: "))
                # make sure that the user input is a positive number
                if (amount > 0):
                    deposite(user_row_index, valid_user, amount)
                else:
                    print('amount must be a positive number')
                    continue
            elif choice == '3':
                withdraw_amount = int(
                    input("Enter the amount you want to withdraw: "))
                # make sure that the user input is a positive number
                if (withdraw_amount > 0):
                    if(float(valid_user[2]) < withdraw_amount):
                        print(
                            "You cannot withdraw amount that's larger than the existing one")
                        continue
                    withdrawal(user_row_index, valid_user, withdraw_amount)
                else:
                    print('amount must be a positive number')
                    continue
                pass
            elif choice == '4':
                print(f"GoodBye, {valid_user[1]}")
                isRunning = False
        # else block to handle user input
    else:
        # print him an error and let him try again
        print('Bank account number is invalid.\nTry again!')
        run()


welcome()
run()
