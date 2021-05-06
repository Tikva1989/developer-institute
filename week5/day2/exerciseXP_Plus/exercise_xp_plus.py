#=============Exercise 1 : Family===============

class Family:

    def __init__(self,last_name):
            self.members =[{'name':'Michael','age':35,'gender':'Male','is_child':False},
                                      {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]
            self.last_name = last_name


    def born(self,  **member):
        self.members.append(member)
        print("Congratulations!!")

    def is_18(self, name):
        for member in self.members:
                if member["name"]== name and  member['age'] >= 18:
                    return True
                else:
                    return False
                    # raise Exception("You are {} years old, you are not allowed to use power!".format(self.members['age']))

    def get_members(self):
        for member in self.members:
            print(f"{member.get('name')}", end=" ")
            print("\n")

#
# family1 = Family("Cool")
# family1.get_members()
#


#==================Exercise 2 : TheIncredibles Family=================



class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self. members =[
    {'name':'Bob','age':35,'gender':'Male','is_child':False,'power':'super-strength', 'incredible_name':'Mr. Incredible'},
    {'name':'Helen','age':32,'gender':'Female','is_child':False,'power':'stretch','incredible_name':'Elastigirl'},
    {'name':'Violet','age':14,'gender':'Female','is_child':True,'power':'invisibility & force field','incredible_name':'Violet'},
    {'name':'Dashiell','age':11,'gender':'Male','is_child':True,'power':'super-speed','incredible_name':'Dash'}
    ]


    def use_power(self, name):
        super().is_18()




    def incredible_presentation(self):
        print(f"Introducing the {self.last_name}'s!")
        for member in self.members:
            print(f"{member['incredible_name']} whose superpower is {member['power']}")



the_incredibles = TheIncredibles("Parr")
# the_incredibles.get_members()
# the_incredibles.incredible_presentation()
jack = {'name':'Baby Jack','age':0,'gender':'Male','is_child':True,'power':'Unknown power','incredible_name':'Jack'}
the_incredibles.born(**jack)
# the_incredibles.get_members()
# the_incredibles.incredible_presentation()
the_incredibles.use_power("Baby Jack")
print(the_incredibles.use_power("Bob"))






