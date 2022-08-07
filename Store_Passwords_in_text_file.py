import random

def otp():
    return random.randint(100000,999999)

def pwd_gen():
    char = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`!@#$%^&*()~-_=+[]\;',./<>?:"{}|"""
    for k in range(1):
        pwd = ''
        for i in range(6):
            pwd += random.choice(char)
    return str(pwd)

user_data = {}

with open('store_pwd.txt','w') as f:
    f.write("This file Stores Passwords\n")
    f.write("When the code is executed\n\n")

while True:
    choose = int(input("Enter 1:sign-up, 2:login, 3:update, 4:delete, 5:quit "))
    print(user_data)
    print("-"*35)

    if choose == 1: # sign-up user
        user_name = input("Enter Name to Signup: ") # sign-up name
        if user_name in user_data.keys():
            print("User Exists")
            print("-"*35)
        else:
            # user choice of password creation
            pwd_choice = int(input("1:User Generated Password 2:Computer Generated Password :: "))
            if pwd_choice == 1:
                pwd = input("Enter your password: ") # user generated password
                user_data[user_name] = pwd
                otp_gen = otp()
                print(f"User generated password: {pwd}")
                print(f"OTP generated for Sign-Up: {otp_gen}")
                print("-"*35)
            else:
                pwd = pwd_gen() # computer generated password
                user_data[user_name] = pwd
                otp_gen = otp()
                print(f"Computer generated password: {pwd}")
                print(f"OTP generated for Sign-Up: {otp_gen}")
                print("-"*35)
                
        with open("store_pwd.txt","a") as fb: # writing the contents of sign-up info to the file
            fb.write("\nRegistered User details are ")
            fb.write(str(user_data))
            fb.write(f"\nOTP Generated is {otp_gen}\n\n")

    if choose == 2: # user login
        user_name = input("Enter Name to Login: ") # login name
        if user_name in user_data.keys():
            pwd = input("Enter Login Password: ")
            if user_data[user_name] == pwd:
                otp_gen = otp()
                print(f"OTP generated for login: {otp_gen}")
                print("Login Success")
                print("-"*35)
            else:
                print("!!! Incorrect Password Given !!!")
                print("-"*35)
        else:
            print("!! User name not found !!")
            print("-"*35)

        with open("store_pwd.txt","a") as fb: # writing the contents of login info to the file
            fb.write("Login User detail is ")
            fb.write(f"\nOTP Generated is {otp_gen}\n\n")

    if choose == 3: # update user
        user_name = input("Enter Name to Update User Password: ") # login name
        if user_name in user_data.keys():
            pwd = input("Enter Login Password to update: ") # login password
            if user_data[user_name] == pwd:
                otp_gen = otp() # generate otp
                print(f"OTP generated for update password: {otp_gen}")
                # user choice of password Creation
                pwd_choice = int(input("1:User Generated Password 2:Computer Generated Password :: " ))
                if pwd_choice == 1:
                    pwd = input("Enter your password: ") # user generated new updated password
                    user_data[user_name] = pwd
                    print(f"User generated new password: {pwd}")
                    print(":) Updated User Info. (:")
                    print("-"*35)
                else:
                    pwd = pwd_gen() # computer generated new updated password
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

        with open("store_pwd.txt","a") as fb: # writing the contents of updated user info to the file
            fb.write(f"\nOTP Generated before updating user {otp_gen}\n")
            fb.write("Updated User details are ")
            fb.write(str(user_data))

    if choose == 4: # delete user
        user_name = input("Enter User-Name to delete: ") # user name to delete  
        if user_name in user_data.keys():
            pwd = input("Enter the password: ") # enter password
            if user_data[user_name] == pwd:
                otp_gen = otp() # generate otp only if the password matches the user name
                del user_data[user_name] # delete the user name from the dictionary 
                print(f"OTP generated before deleting the user details: {otp_gen}")
                print("!!! User data is deleted successfully !!!")
                print("-"*35)
            else:
                print("!!! Incorrect Password Given !!!")
                print("-"*35)
        else:
            print("!! User name not found !!")
            print("-"*35)

        with open("store_pwd.txt","a") as fb: # writing the contents to the file
            fb.write(f"\n\nOTP Generated before deleting user {otp_gen}\n")
            fb.write("Updated User details are ")
            fb.write(str(user_data))


    if choose == 5:
        break

with open("store_pwd.txt","r") as fb: # reading the contents of the file
    print("The contents of the file are: \n")
    read_file = fb.read()
    print(read_file)
