# register
# -firstname, lastname, password
# -generate account number

# login
# - account number and password

# bank operation


# Initializing the system

database = {}

import random


def init():
    print("Welcome to Nations Bank")

    have_account = int(input("Do you have an account with us. (1) Yes (2) No \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()
    else:
        print('You selected an invalid option, try again.')
        init()


def login():
    print('********* Login to your account ********')

    account_number_from_user = int(input('Enter your account number \n'))
    password = input('Enter your password \n')

    for accountNumber, userDetails in database.items():
        if accountNumber == account_number_from_user:
            if userDetails[3] == password:
                bank_operation(userDetails)


        else:
            print('Invalid account number or password, try again.')
            login()


def register():
    print('************ Register an account *************')

    email = input('Enter your email address. \n')
    first_name = input('Enter your first name \n')
    last_name = input('Enter your last name \n')
    password = input('Enter password \n')

    account_number = generate_account_number()

    database[account_number] = [email, first_name, last_name, password, 0]

    print('Your account has been created')
    print('Your account number is: %d' % account_number)
    login()


def bank_operation(user):
    print('Welcome %s %s' % (user[1], user[2]))

    optionSelected = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if optionSelected == 1:
        deposit()

    elif optionSelected == 2:
        withdrawal()

    elif optionSelected == 3:
        logout()

    elif optionSelected == 4:
        exit()

    else:
        print('Invalid option selected, try again')
        bank_operation(user)


def generate_account_number():
    return random.randrange(0000000000, 9999999999)


def deposit():
    print('Deposit Operation')

    for accountNumber, userDetails in database.items():
        current_balance = get_current_balance(userDetails)
        deposit_amount = int(input('Enter the amount you want to deposit: \n'))
        current_balance += deposit_amount

    print('Your current balance is: %d' % current_balance)
    another_transaction()


def withdrawal():
    print('Withdrawal Operation')

    for accountNumber, userDetails in database.items():
        current_balance = get_current_balance(userDetails)

    withdrawal_amount = int(
        input('Enter the amount you want to deposit. (1) 1000 (2) 2000 (3) 5000 (4) 10000 (5)20000 (6) others \n'))

    if withdrawal_amount == 1:
        withdrawal_amount = 1000

    elif withdrawal_amount == 2:
        withdrawal_amount = 2000

    elif withdrawal_amount == 3:
        withdrawal_amount = 5000

    elif withdrawal_amount == 4:
        withdrawal_amount = 10000

    elif withdrawal_amount == 5:
        withdrawal_amount = 10000

    elif withdrawal_amount == 6:
        withdrawal_amount = int(input('Enter amount in multiple of 1000 \n'))

    else:
        print('Invalid option selected, try again')

    if current_balance > withdrawal_amount:
        current_balance -= withdrawal_amount
        print('Your current balance is: %d' % current_balance)

    else:
        print('Insufficient fund')

    another_transaction()


def logout():
    login()


def get_current_balance(user_details):
    return user_details[4]


def another_transaction():
    selected_transaction = int(input('Do you want to perform another transaction. (1) Yes (2) No \n'))

    if selected_transaction == 1:
        login()

    elif selected_transaction == 2:
        exit()

    else:
        print('You have selected an invalid option')


init()
