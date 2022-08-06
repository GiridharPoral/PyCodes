import random

print('Password Generator Program')
print('-'*30)

# char is characters available to generate a strong password
char = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`!@#$%^&*()~-_=+[]\;',./<>?:"{}|"""

# How many Passwords to create
number = int(input("How many passwords to generate: ")) 

# Length of the password
length_pwd = int(input("Password Length: "))
print('\nThe passwords are generated below: ')

for pwd in range(number): # number of passwords
    passwords = '' # empty password string

    for c in range(length_pwd): # length of password
        passwords += random.choice(char) #Password is created using char

# Passwords Printed        
    print(passwords)
