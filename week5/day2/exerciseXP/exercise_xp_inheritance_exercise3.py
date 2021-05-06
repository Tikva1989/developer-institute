import exercise_xp_inheritance
import random

#================================Exercise 3 : Dogs Domesticated===================

class PetDog(exercise_xp_inheritance.Dog):
    def __init__(self, name, age, weight):
        self.trained =  False
        self.name = name

    def train(self):
        exercise_xp_inheritance.Dog.bark(self)
        if self.trained == True :
            self.trained = False
        elif self.trained == False:
            self.trained = True

    def play(self, *args):
        names= []
        for args in args:
          name = args.name
          names.append(name)
        print(f'{names} all play together')


    def do_a_trick(self):
        my_sentence = [f'{self.name} does a barrel roll', f'{self.name} stands on his back legs', f'{self.name} shake your hands', f'{self.name} plays dead']
        while self.trained == True:
            print(random.choice(my_sentence))
            break

Rex =PetDog("Rex", 12, 20)
Bengi = PetDog("Bengi" , 10, 30)
Dud =  PetDog("Dud" , 15, 50)
print(Rex)
Rex.play(Bengi, Dud)

Rex.train()
print(Rex.trained)
Rex.do_a_trick()



