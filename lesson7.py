#!/usr/bin/python

#####################
#   Dictionaries
#   Name : Andrea Kitonga
#   Date : 23 / 5 / 2022



#Initializing Dictionaries
from email.errors import MissingHeaderBodySeparatorDefect


student = {"Name" : "Andrea" , "age" : 18 , "gender" : "female"}
print(student["Name"])
print(student["age"])
print(student["gender"])
student["Id.No"] = "30479471"
student["Hobby"] = "Football"
student["Club"] = "Drama"
student["colour"] = "Midnight Blue"
student["movie"] = "The Italian Job "
print(student) 


 #startng with empty dictionary

student = {}
student = ()
print("The first student")
student["favfood"] ="Chapati"
student["homecity"] = "Machakos"


#modify values
student["Name"] = "Maddy"
