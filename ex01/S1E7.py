
from S1E9 import Character


class Baratheon(Character):
    '''Child- Baratheon class'''
    def __init__(self, first_name, is_alive=True):
        '''Baratheon constructor'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        '''Baratheon __str__- informal'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Baratheon Repr - formal"""
        return self.__str__()

    def die(self):
        self.is_alive = False


class Lannister(Character):
    '''Child- Lannister class'''
    def __init__(self, first_name, is_alive=True):
        '''Lannister constructor'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        '''Lannister __str__ - informal'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        '''Lannister __repr__ - formal'''
        return self.__str__()

    def die(self):
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        '''Static method- to create a Lannister character'''
        return Lannister(first_name, is_alive)

    # OR
    # @classmethod
    # def create_lannister(cls, first_name, is_alive = True):
    #     '''Class method- to create a Lannister character'''
    #     return cls(first_name, is_alive)
