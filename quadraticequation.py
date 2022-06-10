import math

a = int(input("Enter the coefficient of the first term"))
b = int(input("Enter the coefficient of the  second term"))
c = int(input("Enter the constant of the fisrt term"))
w = math.sqrt((b**2)-4*a*c)
y1 = (-b + math.sqrt((b**2) -4*a*c))/(2*a)
y2 = (-b - math.sqrt(b**2) -4*a*c)/(2*a)

y_1 = (-b+w)/(2*a)
y_2 = (-b-w)/(2*a)



print("The roots of the quadratic equtions are :",y1,y2)