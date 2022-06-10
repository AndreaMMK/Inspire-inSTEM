#!/usr/bin/python
#Functions in python
#Name :Andrea Kitonga
#Date:31/05/2022

#block of code that can be executed together
#initializing functions
#calling functions


def say_hello () :
    print("Hello!")
    x=4
    y=7
    z=x+y
    print(z)
say_hello()

def bark():
    print("Dogs bark woof woof")    
bark()

def meow():
    print("Cats meow meow")
meow()


def moo():
    print("Cows moo moo")
moo()

def bray():
    print("Donkeys bray bray")
bray()
   
def add_numbers (x,y):
    sum_nums = x+y
    print("The sum of numbers :", sum_nums)

add_numbers (40,50)
add_numbers (100,400)
add_numbers(1,4)


def prod_numbers (x,y):
    prod_nums = x*y
    print("The product of numbers :", prod_nums)

    prod_nums (40,50)
    prod_nums  (100,400)
    prod_nums  (1,4)




    
import math
def find_roots(a,b,c):
        y1 = (-b + math.sqrt((b**2) -(4*a*c)))/(2*a)
        y2 = (-b - math.sqrt((b**2) -(4*a*c)))/(2*a)

        print("The roots of the quadratic")





