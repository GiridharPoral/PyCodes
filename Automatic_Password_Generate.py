import random

# Generate OTP Function
def otp():
    return random.randint(100000,999999) # returns 6-digit OTP

# Generate Password Function
def pwd_gen():
    char = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`!@#$%^&*()~-_=+[]\;',./<>?:"{}|"""
    for k in range(1):
        pwd = ''
        for i in range(6):
            pwd += random.choice(char)
    return pwd # returns 1 random generated password

user_data = {} # Empty Dictionary

while True:
    choose = int(input("Enter 1:sign-up, 2:login, 3:update, 4:delete, 5:quit "))
    print(user_data)
    
    if choose == 1: # user signup
        user_name = input("Enter Name to Sign-Up: ")
        if user_name in user_data.keys():
            print("User Exists!")
        else:
            pwd = pwd_gen() # Generate Strong Password
            user_data[user_name] = pwd
            print(f"Computer generated password is {pwd}")
            print(f"OTP generated for Sign-Up: {otp()}")

    if choose == 2: # user login
        user_name = input("Enter Name to Login: ")
        if user_name in user_data.keys():
            pwd = input("Enter Login Password: ")
            if user_data[user_name] == pwd:
                print(f"OTP generated for login: {otp()}")
                print("Login Success")
            else:
                print("!!! Incorrect Password Given !!!")
        else:
            print("!! User name not found !!")

    if choose == 3: # update user
        user_name = input("Enter Name to Update User Password: ")
        if user_name in user_data.keys():
            pwd = input("Enter Login Password to update: ")
            print(f"OTP generated for update password: {otp()}")
            if user_data[user_name] == pwd:
                new_pwd = pwd_gen() # generates new password again
                user_data[user_name] = new_pwd
                print(f"Computer generated updated password is {new_pwd}")
                print(":) Updated User Info. (:")
            else:
                print("!!! Incorrect Password Given !!!")
        else:
            print("!! User name not found !!")

    if choose == 4: # delete User
        user_name = input("Enter Name to Delete User Password: ")
        if user_name in user_data.keys():
            pwd = input("Enter Login Password to delete: ")
            if user_data[user_name] == pwd:
                del user_data[user_name]
                print(":( user deleted")
            else:
                print("!!! Incorrect Password Given !!!")
        else:
            print("!! User name not found !!")
                
    if choose == 5: # Come out of While Loop
        break
