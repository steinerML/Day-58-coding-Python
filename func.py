#Functions

#Defining a function

def greet_user():
    '''Display a greeting'''
    print("Hello there!")

greet_user()

#Passing an argument

def greet_user(username): #Argument that will be taken by function
    '''We display a personalized greeting now'''
    print("Hello there",username)

greet_user('James Bond')
greet_user('Adolf')
greet_user('Vladimir')

#Passing positional arguments: when function is called parameters need to be in the same order as they appear in function definition'''

def describe_pet(animal,name):
    '''Display info about a pet'''
    print('\nI have a ' + animal)
    print('Its name is ' + name )

describe_pet('Dog','Joe Biden')
describe_pet('Pig', 'Barack')
describe_pet('Bald Eagle', 'Trump')

#Passing keyword arguments: parameters need to be in order and accompanied by the equal sign and''' 

def describe_car(brand,color):
    '''Display info about a pet'''
    print('\nI have a ' + brand)
    print('Its color is ' + color )

describe_car(brand='Porsche', color='Matt grey')
describe_car(brand='Ferrari', color='Rosso Corsa')

#Default values for Parameters

def describe_pet(name,animal='Dog'):
    '''Display info about a pet'''
    print('\nI have a ' + animal)
    print('Its name is ' + name )

describe_pet('Bobby')
describe_pet('Slippy','Fish')
describe_pet('Johnny')

#Optional arguments using None

def describe_pet(animal,name=None):
    '''Display info about a pet'''
    print('\nI have a ' + animal)
    if name:
        print('Its name is '+ name )

describe_pet('Dog')
describe_pet('Cat')
describe_pet('Fish', 'Wetty')
