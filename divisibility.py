#Write a program to check whether a number is divisible by 5 or 7
num = int(input("The number is "))
if (num%7 == 0) and (num%5 == 0) :
    print(f"Number is divisible by both 7 and 5")
else:
    print(f"Number is not divisible by both 7 qnd 5")
    
if (num%5 == 0):
    print(f"Number is divisible by 5")
else:
    print(f"Number is not divisible by 5")

if (num%7 == 0):
    print(f"Number is divisible by 7")
else: 
    print(f"Number is not divisible by 7")