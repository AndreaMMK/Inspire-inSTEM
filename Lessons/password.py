import random
print('Welcome to a password generator')
character = ''
num_password = int(input("How many passwors do they want generated ?"))
len_password = int(input("Ask user for password length?"))
print(num_password)
print(len_password)
for password in range(num_password):
   password = ''
for c in range (len_password):
    password += random.choice(character)
print(password)


