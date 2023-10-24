# A password protected entry system

import json
json_link = '/Users/Matt/OneDrive - Staffordshire University/University/Year 1/Software Development And Application ' \
            'Modelling/SDAM/week10/security_checker_users.json'


def output_main_menu():
    print("""Choose one of the following options:
    1. New user
    2. Existing user""")


def choose_option():
    choice = 0

    while choice != 1 and choice != 2:
        try:
            choice = int(input("Enter choice: "))
            if choice != 1 and choice != 2:
                raise Exception

        except ValueError:
            print("You need to enter an integer")

        except Exception:
            print("You need to enter 1 or 2")

    if choice == 1:
        choice1()

    else:
        confirm_username_and_password()


def choice1():
    username_login = input("Enter username: ")
    password_login = check_password()

    while password_login is False:
        password_login = check_password()

    reenter_password = input("Re-enter new password: ")

    while reenter_password != password_login:
        print("Passwords do not match")
        reenter_password = input("Re-enter new password: ")

    save(username_login, password_login)
    print()
    output_main_menu()
    choose_option()


def check_password():
    new_password = input("Enter new password: ")
    if len(new_password) == 0 or ' ' in new_password or new_password[0].isdigit() or len(new_password) < 8:
        print("Invalid password")
        new_password = False
    return new_password


def save(username, password):
    new_data = {
        username: {
            "password": password
        }
    }

    try:
        with open(json_link, 'r') as f:
            data = json.load(f)

    except FileNotFoundError:
        with open(json_link, "w") as f:
            json.dump(new_data, f, indent=2)

    else:
        data.update(new_data)
        with open(json_link, "w") as f:
            json.dump(data, f, indent=2)


def confirm_username_and_password():
    password_match = False
    password_count = 0

    while password_match is False and password_count < 3:
        confirm_username = input("Enter a username: ")
        confirm_password = input("Enter a password: ")

        try:
            with open(json_link, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("No data file found.")
        else:
            if confirm_username in data:
                actual_password = data[confirm_username]["password"]

                if actual_password == confirm_password:
                    print("Welcome")
                    password_match = True
                else:
                    print("Incorrect password")
                    password_count += 1

            else:
                print("Incorrect username")

    if password_count > 2:
        print("You have had too many attempts and are now locked out")


output_main_menu()
choose_option()
