#/user/bin/python

#########################################################
#lesson:operations.py
#Name : Andrea Kitonga
#Date : 6/6/22
#########################################################

f = open("lesson.txt")
f = open("lesson2.txt",)
#read line by line

print(f.readline())

with open("lesson2.txt",'r+w')as f:
     f.write("This is my new file\n")
     f.write("I am from Nairbi\n")
     f.write("Today is a good day\n")

#reading the file
print(f.read())
f.close()

#opening file
