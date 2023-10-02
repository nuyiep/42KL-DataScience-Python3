
from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
# __dict__ is a special attribute of an object 
# that returns a dictionary containing the object's 
# attributes (names) and their corresponding values
print(Ned.is_alive)
Ned.die() 
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
