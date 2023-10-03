
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King class'''
    def __init__(self, first_name, is_alive=True):
        '''King constructor'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        '''Set new eye color'''
        self.eyes = new_eyes

    def get_eyes(self):
        '''Get new eye color'''
        return (self.eyes)

    def set_hairs(self, new_hair):
        '''Set new hair'''
        self.hairs = new_hair

    def get_hairs(self):
        '''Get new hair'''
        return (self.hairs)
