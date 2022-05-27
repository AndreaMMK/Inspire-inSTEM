# A dictionary is a collection of key value pairs
 # syntax :dictionary ={'key' :'value'}
list_names = "Andrea MMK"
colors = {'color' : 'red'}
vehicle = {'type' :'toyota' ,'plate_number ' :  'KYZ954P'}
print(colors)


#print (type(colors)) # We use the type method to read the data
# accesing values in a dictionary

print(vehicle['type'])  #You can access the value of an element inside a dictionary using the key
print(vehicle['type' and 'plate_number '])


person = {'name' : 'Andrea' , 'P_number' : '45678974' , 'gender ' :'female' , 'address' :'567-0200'}
print(person['name'])
print(person['P_number'])
print(person['gender '])
print(person['name' and 'P_number' and 'gender' and 'address'])

#adding to a dictionary
person['age'] = '18'
print(type(person))
print(person)


print(person['name'], str(['age']))

#deleting from a dictionary
del[person['P_number']]
print(person)

#looping over dictionaries
for key ,value in person.items(): 
    print(f"{value}: {key}")
colors =["red","green","blue","purple"]

i = 1
while i < len(colors):
    if(colors[1]=='green'):
        print(colors[1].upper())
        i += 1 

for color in colors:
    if(colors[0] == "red"):
        print(colors[0].upper())
        i += 1
        
for color in colors:
    if(colors[0] == "blue"):
        print(colors[0].upper())
        i += 1
        
for color in colors:
    if(colors[0] == "purple"):
        print(colors[0].upper())
        i += 1


print("person.get('password'the 'location' key is non existent")

mary_fav_food = ['beef','chiken','vegetable']
jane_fav_food = ['rice','ugali','potatoes']
#dictionary containing the above
food={
    'mary':['beef','chiken','vegetable'],
    'jane':['rice','ugali','potatoes'],
}
print(food)
# list in dictionaries
# person (name,email,password)
person= {
    'joy':['name','email','password']
}
print(person)


