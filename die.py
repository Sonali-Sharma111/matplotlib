from random import randint
class Die:
    
    '''A class representing a single Die'''
    def __init__(self,num_sides=8):
        '''Assume a six-sided Die.'''
        self.num_sides=num_sides
    def roll(self):
        """return a random value between 1 and number of sides"""
        return randint(1,self.num_sides)
        