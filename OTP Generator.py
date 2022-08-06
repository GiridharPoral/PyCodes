import random

def otp():
    # returns a 6 digit OTP
    return random.randint(100000,999999)

print("6-Digit OTP Generated is {}".format(otp()))
