import random

# Generate OTP Function
def otp():
    return random.randint(100000,999999)

# Generate Password Function
def pwd_gen():
    char = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`!@#$%^&*()~-_=+[]\;',./<>?:"{}|"""
    for k in range(1):
        pwd = ''
        for i in range(6):
            pwd += random.choice(char)
    return pwd

user_data = {}

while True:
    choose = int(input("Enter 1:sign-up, 2:login, 3:update, 4:delete, 5:quit "))
    print(user_data)
    print("-"*35)

    if choose == 1: # sign-up user
        user_name = input("Enter Name to Signup: ")
        if user_name in user_data.keys():
            print("User Exists")
            print("-"*35)
        else:
            pwd_choice = int(input("1:User Generated Password 2:Computer Generated Password :: "))
            if pwd_choice == 1:
                pwd = input("Enter your password: ")
                user_data[user_name] = pwd
                print(f"User generated password: {pwd}")
                print(f"OTP generated for Sign-Up: {otp()}")
                print("-"*35)
            else:
                pwd = pwd_gen()
                user_data[user_name] = pwd
                print(f"Computer generated password: {pwd}")
                print(f"OTP generated for Sign-Up: {otp()}")
                print("-"*35)
                
    if choose == 2: # user login
        user_name = input("Enter Name to Login: ")
        if user_name in user_data.keys():
            pwd = input("Enter Login Password: ")
            if user_data[user_name] == pwd:
                print(f"OTP generated for login: {otp()}")
                print("Login Success")
                print("-"*35)
            else:
                print("!!! Incorrect Password Given !!!")
                print("-"*35)
        else:
            print("!! User name not found !!")
            print("-"*35)

    if choose == 3: # update user
        user_name = input("Enter Name to Update User Password: ")
        if user_name in user_data.keys():
            pwd = input("Enter Login Password to update: ")
            print(f"OTP generated for update password: {otp()}")
            if user_data[user_name] == pwd:
                pwd_choice = int(input("1:User Generated Password 2:Computer Generated Password :: " ))
                if pwd_choice == 1:
                    pwd = input("Enter your password: ")
                    user_data[user_name] = pwd
                    print(f"User generated new password: {pwd}")
                    print(":) Updated User Info. (:")
                    print("-"*35)
                else:
                    pwd = pwd_gen()
                    user_data[user_name] = pwd
                    print(f"Computer generated new password: {pwd}")
                    print(":) Updated User Info. (:")
                    print("-"*35)

            else:
                print("!!! Incorrect Password Given !!!")
                print("-"*35)
        else:
            print("!! User name not found !!")
            print("-"*35)

    if choose == 4: # delete user
        user_name = input("Enter User-Name to delete: ")
        if user_name in user_data.keys():
            pwd = input("Enter the password: ")
            if user_data[user_name] == pwd:
                del user_data[user_name]
                print("!!! User data is deleted successfully !!!")
                print("-"*35)
            else:
                print("!!! Incorrect Password Given !!!")
                print("-"*35)
        else:
            print("!! User name not found !!")
            print("-"*35)

    if choose == 5:
        break
