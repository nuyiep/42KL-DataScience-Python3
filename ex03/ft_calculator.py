

class calculator:
    '''Calculator class'''
    def __init__(self, vectorX):
        '''Calculator constrctor'''
        self.vectorX = vectorX

    def __add__(self, scalarZ) -> None:
        ''' __add__ is a special method in Python'''
        self.vectorX = [i + scalarZ for i in self.vectorX]
        print(self.vectorX)

    def __mul__(self, scalarZ) -> None:
        '''Multiply'''
        self.vectorX = [i * scalarZ for i in self.vectorX]
        print(self.vectorX)

    def __sub__(self, scalarZ) -> None:
        '''Subtraction'''
        self.vectorX = [i - scalarZ for i in self.vectorX]
        print(self.vectorX)

    def __truediv__(self, scalarZ) -> None:
        '''Division- handle 0 division'''
        try:
            self.vectorX = [i / scalarZ for i in self.vectorX]
            print(self.vectorX)
        except ZeroDivisionError as err:
            print(f"ERROR! {err}")

# __add__ is a special method in Python
# For this exercise, we want to overide the __add__ function
# So, when you write v1 + 5, Python recognizes that v1 is an
# instance of the calculator class, and the + operator triggers
# the __add__ method of the calculator class.
