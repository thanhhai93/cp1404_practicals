def get_password():
    """ User input password and check if requirements met"""
    global password
    password = input("Enter your password: ")
    while len(password) < 10:
        print("Your password does not meet the requirements")
        password = input("Enter your password: ")

def main():
    print("Your password must be at least 10 characters long")
    get_password()

    print("*" * len(password))

if __name__ == '__main__':
    main()