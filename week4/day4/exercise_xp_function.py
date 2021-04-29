#                      Exercise XP Functions:
# Exercise 1 : What Are You Learning ?   write my first function:
# def display_message():
#     print("I\'m learning Python language")
#
# display_message()

# #   Exercise 2: What’s Your Favorite Book ?
#
# def favorite_book(title):
#      print(f'One of my favorite books is {title}')
#
# favorite_book("Alice in Wonderland")

# # Exercise 3 : Some Geography
# def describe_city(city, country= "Israel"):
#     print(f'{city} is in {country}')
#
# describe_city("Tel-aviv", "Israel")

# #   Exercise 4 : Random
# import random
# def rand_num(num):
#
#     '''Info: Create a function that accepts a number between 1 and 100 and generates another number randomly
#      between 1 and 100. Compare the two numbers, if it’s the same number, display a success message,
#      otherwise show a fail message and display both numbers.'''
#
#     machine_rand = random.randrange(1, 100)
#     if num == machine_rand :
#         print(f'success, numbers are the same')
#     else:
#         print(f'Fail, numbers are not the same')
#         return num, machine_rand
#
# print(rand_num(20))

#   Exercise 5 : Let’s Create Some Personalized Shirts
# # #1 craet function
# def make_shirt(size, text):
#     print(f'Your size is {size}, printig : {text}')
#     return text
#
# print(make_shirt("S", "I love coding"))

# # 2.
# def make_shirt(size = "L", text = "I love Python"):
#       ''' Info: make shirt withe default size L and text : I love Python'''
#       print(f'Your size is {size}, printig : {text}')
#
# make_shirt()
# make_shirt(size="M")
# make_shirt(size="S", text=" I !== Hate Python")
# make_shirt(text="Keyword Argument Rock!!", size= "M")   #Bounus

#       Exercise 6 : Magicians …
magicians = ["harry houdini", "david blaine", "david copperfield"]
def show_magicians(magicians):
    '''Info: make a list of names fot a given list'''
    for magician in magicians:
        print(magician)

# show_magicians(magicians)
def make_great(magicians):
    '''info: add " the Geart" to evry magician in list'''
    great_magicians = []

    while magicians:
        # Make each magician great, and add it to great_magicians
        magician = magicians.pop()
        great_magician = magician + "the Great"
        great_magicians.append(great_magician)
    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)


make_great(magicians)
show_magicians(magicians)




