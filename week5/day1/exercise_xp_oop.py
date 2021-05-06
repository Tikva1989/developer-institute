# #    Exercise 1: Cats
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_detail(self):
#         print(f'{self.name}, {self.age}')
#
# cat_1 = Cat('Herzel', 2)
# cat_2=Cat('David', 1)
# cat_3=Cat('Moly', 3)
#
# # cat_1.show_detail()
# # cat_2.show_detail()
# # cat_3.show_detail()
#
#  # Outside of the class, create a function that finds the oldest cat and returns the cat.
# def oldest_cat(*args, **kwargs):
#     max_age = max(kwargs.values())
#     for key, value in kwargs.items():
#         if value == max_age:
#
#             print(f' The oldest cat is {key} and {max_age} years old')
#
#
#
# oldest_cat(cat_1=cat_1.age, cat_2=cat_2.age, cat_3=cat_3.age)

#  Exercise 2 : Dogs
#Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print(f'{self.name} goes woof!')
#
#     def jump(self):
#         x = int(self.height) * 2
#         print(f'{self.name} jumps {x} cm heigh!')
#
#
#
# #Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# # Print the details of his dog (ie. name and height) and call the methods bark and jump.
#
# daivids_dog= Dog("Rex", 50)
# print(f'daivids dog name is {daivids_dog.name} and his height is {daivids_dog.height} cm')
# daivids_dog.bark()
# daivids_dog.jump()
#
# # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# # Print the details of her dog (ie. name and height) and call the methods bark and jump.
# sarahs_dog = Dog("Teacup", 20)
# print(f'sarahs dog name is {sarahs_dog.name} and his height is {sarahs_dog.height} cm')
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
# if daivids_dog.height > sarahs_dog.height:
#     print(daivids_dog.name )
# else:
#     print(sarahs_dog.name)

# ====================Exercise 3 : Who’s The Song Producer?================
#Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
#
# class Song:
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for elem in self.lyrics:
#             print (elem)
#
## stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

#================================Exercise 4 : Afternoon At The Zoo================

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animals_list= []

    def add_animal(self, new_animal):
        while new_animal not in self.animals:
            self.animals_list.append(new_animal)
        else:
            print(f'{new_animal}  allready exiest')

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals_list:
            self.animals_list.remove(animal_sold)


ramat_gan_safari= Zoo("ramat_gan_safari")
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Eal')
ramat_gan_safari.add_animal('Emu')








