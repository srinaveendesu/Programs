# Creational Pattern
# Encapsulates Object creation. That is factory is an object specializing
# in creating another object

# Problem
#    When unsure of type of objects needed eventually in the system
#    Decisions to be made at run time for what class to use
# It does not rely on polymorphism

class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"

class Cat:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"

def get_pet(pet="dog"):

	"""The factory method"""

	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

	return pets[pet]

d = get_pet("dog")

print(d.speak())

c = get_pet("cat")

print(c.speak())


# Woof!
# Meow!



