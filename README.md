# 42KL-DataScience-Python3
Oriented Object Programming
	- classes and heritage

**ex00** 
__dict__ is a special attribute of an object that returns a dictionary containing the object's attributes (names) and their corresponding values
# @abstractmethod - @ is a decorator
decorator https://www.youtube.com/watch?v=BE-L7xu8pO4

**ex01**
__str__ and __repr__ 
		- special method (magic method/dunder method)
		- customize string representation of an object
__str__ - user-friendly, informal string representation 
__repr__ - formal and unambiguous string representation
class method - when you want to use a class variable
			 - https://www.youtube.com/watch?v=lVfGQOzzRCM&ab_channel=Telusko
static method - not object not class 
			  - no self no cls

**ex02**
Diamond inheritence - where a class inherits from two or more classes
    A
   / \
  B   C
   \ /
    D
Method Resolution Order- MRO
	- C3 linearization algorithm is used to determine the MRO
	- ensures that method and attribute resolution occurs in a
	  consistent and predictable way, avoiding conflicts in cases
	  of multiple inheritence and diamond inheritence hierarchies
	Rules
	- Base classes are searched from left to right according to the 
	  order in which they are listed in the class definition
	- The C3 Linearization algorithm ensures that classes are 
	   searched in a consistent and predictable order, even in 
	   complex multiple inheritance scenarios.
	- print(MyClass.mro())
