class Farm:
    def __init__(self, name,  animals={}):
        self.name= name
        self.animals = animals

    def add_animal(self, animal , amount = 1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self):
        output_class =  '''f'
        {self.name}\'s farm
            '
    E-I-E-I-0!
        '''