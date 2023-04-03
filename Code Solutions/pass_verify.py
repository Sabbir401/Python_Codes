# import re

# def check_password(password):
#     if len(password) < 6 or len(password) > 12:
#         return False
    
#     if not re.search("[a-z]", password):
#         return False
    
#     if not re.search("[0-9]", password):
#         return False
    
#     if not re.search("[A-Z]", password):
#         return False
    
#     if not re.search("[$#@]", password):
#         return False
    
#     return True

# passwords = input("Enter comma separated passwords: ")
# password_list = passwords

# valid_passwords = []
# for password in password_list:
#     if check_password(password):
#         valid_passwords.append(password)

# print(",".join(valid_passwords))

import re

def check_pass(x):
    if len(x) < 6 or len(x) > 12:
        return False
    
    if not re.search("[a-z]", x):
        return False
    
    if not re.search("[0-9]", x):
        return False
    
    if not re.search("[A-Z]", x):
        return False
    
    if not re.search("[$#@]", x):
        return False
    
    return True

password = input("Enter comma separated passwords: ").split(",")

valid_pass = []
for i in password:
    if check_pass(i):
        valid_pass.append(i)

print(valid_pass)