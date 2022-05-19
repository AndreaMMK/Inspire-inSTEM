# learning about lists
from asyncio.proactor_events import _ProactorDuplexPipeTransport


motorcycle_owner = "Moto Jojo"
plate_number =  [ 'H1234' ,'Y1234' ,'S1234']
motorcycle = ['honda','yamaha','suzuki']
# accessing list items using the index
print ( motorcycle) 
print (motorcycle[1])
print (motorcycle [2])
motorcycle[0] = "bugati"
print(motorcycle)
motorcycle [1] = "bugati" # changing element in a list
print(motorcycle)
#adding element in a list
print("I love my" + str( motorcycle [1]))
motorcycle.append( ' bugati yamaha') #adding an item to a list
print (motorcycle)
print (motorcycle[0] + plate_number[0])
print(motorcycle [1] + plate_number [1])
print(motorcycle [2] + plate_number [2])
# delete item from a list
del motorcycle [0]
print (motorcycle)
popped_motorcycle =  motorcycle.pop()
print(popped_motorcycle)
# print a statement with the name, motorcycle and plate number
print("My name is " +  motorcycle_owner + " and I own a " + motorcycle [1]  + plate_number [1] )
print (f"My name is  {motorcycle_owner}   and I own a  {motorcycle [1]}  {plate_number[1]}")
motorcycle .remove('suzuki')
print (motorcycle)
school = [ 'Joy' ,'Hope' , 'Mercy' , 'Happy']
pupil = [ 'Peace' , 'Patience' , 'Amani' , 'Keziah']
print("I am (pupil{0}) and I school at (school {0})")
print("I am (pupil{1}) and I school at (school {1})")
print("I am (pupil{2}) and I school at (school {2})")
print("I am (pupil{3}) and I school at (school {3})")
for pupil in  pupil :
 print("Hello i am pupil (pupil)")



