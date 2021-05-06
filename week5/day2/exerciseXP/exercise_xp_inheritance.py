import random
# ===========Exercise 1 : Pets==========

# # Add another cat breed.
# # Create a list of all of the pets. Name the list my_cats = [].
# # Instantiate the Pet class with all your cats. Use the my_pets variable.
# # Take all the cats for a walk, use the walk method.
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# #new cat breed
# class Korat(Cat):
#     def sing(selfself, sounds):
#         return f'{sounds}'
#
# c1 = Cat("Madonna", 1)
# c2 = Cat("Britny", 2)
# c3 = Cat("Whitney", 3)
# my_cats = [c1, c2, c3]
# # print(my_cats)
#
# my_pets = Pets(my_cats)
# # from my_cats list
# # print(my_pets.walk())
# # from each cat itself:
# print(c1.walk())
# print(c2.walk())
# print(c3.walk())

#========================Exercise 2 : Dogs=====================


class Dog:
    def  __init__(self, name, age, weight):
        self.name= name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        run_speed = int(self.weight) / int(self.age)* 10
        return run_speed

    def fight(self, other_dog):
        this_dog =  self.run_speed()* self.weight
        other_dogs = other_dog.run_speed()* int(other_dog.weight)
        if this_dog > other_dogs:
            print( f'{self.name} is the winner')
        else:
            print(f' {other_dog.name} is the winner')

d1= Dog("Marly", 2, 10)
d2 = Dog("Bob", 4, 20)
d3 = Dog("Rasta", 8, 30)

# d1.bark()
# d2.bark()
# d3.bark()
#
# print(d1.run_speed())
# print(d2.run_speed())
# print(d3.run_speed())
#
# print(d1.fight(d2))
# print(d2.fight(d3))
# print(d3.fight(d1))











