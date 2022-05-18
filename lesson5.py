 # methods
name = "andrea kitonga"
name = "lovella"

user_name = " lovella "
age = 19
age = 55
person = "i am" + str(name) + "and my age is" + str(age)
#print ("i am " + str(name) + "and my age is" + str(age)
# the format method
# newline \n and tab \t
print(f"my \t name is {name} \n and i am {age} years old ")
print(user_name)
print(name)
print(name,age)
print(user_name.strip)
print(user_name.lstrip())

#multiple line
msg = """QETRUIOE2746KJ MPESA confirmed you have received
 5000 from  Ntional Bank Of Kena
  on 26th June."""

city = "nairobi"
print(city[:5])
print(city[-1])

f_name = "andrea kitonga" #small letters
#.upper() convert to upper case
print(f_name.upper())

s_name = "ANDREA KITONGA"
# .lower() convert to lower case

print(s_name.lower())
#concertination .converting from one data type to another
# int -> float  float(x)
#float -> int    int(x)
#int -> string   str(x)

number = 4
print(str(number))
x = 4 #x is an integer
print(float(x))
y = 3.5
print(int(y))

f_name = "andrea"
s_name = "kitonga"
full_name = f_name + s_name
print(full_name) 
name = "andrea kitonga"
print(name.replace('a','f'))
msg = "hello i love music"
print(msg.split())
print(len(msg))