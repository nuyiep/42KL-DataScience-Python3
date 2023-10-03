
from abc import ABC, abstractmethod
# abc- abstract base class


class Character(ABC):
    '''Abstract class'''
    @abstractmethod
    # @ decorator https://www.youtube.com/watch?v=BE-L7xu8pO4
    def __init__(self, first_name, is_alive=True):
        '''Constructor- allows you to initialize the
        state of an object when it is created'''
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    '''Child class'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor- allows you to initialize the
        state of an object when it is created'''
        super().__init__(first_name, is_alive)
        # calls the constructor of the parent using super()
        self.is_alive = is_alive

    def die(self):
        '''(Method) Die - Set is_alive to False'''
        self.is_alive = False
