#
def print_name(name ="Andrea Kitonga"):
    print(name)
print_name()
print_name("Gloria")

def get_sum(num_1,num_2):
    sum_nums = num_1 + num_2
    return sum_nums

print(get_sum(7,12))

#Write a function that gets the square of numbers
def powers(number,power):
    power_number = number**power
    return power_number
print(powers(6,4))

def get_full_name(f_name,s_name):
    full_name = f_name + " " + s_name
    return full_name.title()
print(get_full_name("Andrea","Kitonga"))


#returnng a dictionary from a function
def create_full_name(f_name,s_name):
    person = {'Andrea':f_name,'Kitonga':s_name}
    return person
student = create_full_name("Andrea","Kitonga")
print(student)

#parsing a list in a function
def greet_friends(names):
    for name in names:
    msg = "Hello!"+ name.title() + "!"
    print(msg)

    friends = ['Jewel','Chris','Harriet']
    greet_friends(friends)
    