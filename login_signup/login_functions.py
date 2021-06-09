import os

import time


def clear():

    os.system('cls')


failed = 0


def signup():

    global failed

    # open files

    account_check = open('text_files/login_text/account.txt', 'a')

    recover_check = open('text_files/login_text/recover_account.txt', 'a')

    while True:

        time.sleep(2)
        clear()

        email = input("Enter your email so that we can send your account info in case you forgot: ")

        email_check = open('text_files/login_text/email.txt', 'r')

        DOA = email_check.readlines()

        if email.strip() in DOA:

            print('Email already in use!')

        else:

            email_check = open('text_files/login_text/email.txt', 'a')

            email_check.write(email)

            username = input("Enter a username: ")

            user_check = open('text_files/login_text/username_check.txt', 'r')

            DOU = user_check.readlines()

            if username.strip() in DOU:

                print("Username taken!")

            else:

                user_check = open('text_files/login_text/username_check.txt', 'a')

                user_check.write('\n')

                user_check.write(username)

                user_check.close()

                password = input("Enter a strong password or just press enter to randomly make a password: ")

                if password == '':
                    import random

                    actual = 0

                    char = "abcdefghijklmnopqrstuvwxyz1234567890@"

                    for x in username:
                        actual += 1

                    password = "".join(random.sample(char, actual))
                    print("Password: "+str(password))

                    account_check.write('\n')

                    account_check.write(f'{username} : {password}')

                    account_check.close()

                    recover_check.write(f'{email}=username is {username} and password is {password}')

                    recover_check.write('\n')

                    recover_check.close()

                    print("Now login!")

                    login()

                else:
                    confirm = input("Confirm password: ")

                    if password == confirm:

                        account_check.write('\n')

                        account_check.write(f'{username} : {password}')

                        account_check.close()

                        recover_check.write(f'{email}=username is {username} and password is {password}')

                        recover_check.write('\n')

                        recover_check.close()

                        print("Now login!")

                        login()

                    else:

                        print("Passwords do not match!")


def login():

    while True:

        time.sleep(2)

        clear()

        username = input("Enter username: ")

        password = input("Enter password: ")

        account = open("text_files/login_text/account.txt", "r")

        data = account.readlines()

        if username + ' : ' + password in data:

            print("Access granted...")

            quit()

        else:

            print("Invalid")


def forgot():
    all_data = {}

    with open("text_files/login_text/recover_account.txt") as f:

        for line in f:

            (key, val) = line.split('=')

            all_data[key] = str(val)

    while True:

        time.sleep(2)

        clear()

        email = input("Enter email: ")

        if email in all_data:

            data = all_data.get(email)

            print(data)

            print("Now login! YOU BETTER REMEMBER NEXT TIME! ")

            login()

        else:

            print("Invalid email.")
