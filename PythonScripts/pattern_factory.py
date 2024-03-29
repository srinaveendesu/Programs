# Creational Pattern

# Factory encapsulates object creation. That is, Factory
# is an object specializing in creating other objects.
# The Factory pattern is useful, especially when you're
# not sure about what type of objects you'll be needing
# eventually in your system. Another possibility is the
# situation in which your application needs to decide on
# what class to use at run time. Here is a scenario we'll be
# using in our coding exercise. Your pet shop was only selling
# dogs but now you need to sell cats, too. Therefore, your system
# needs to be able to handle cats as well as dogs.
#
# Your system's supposed to show how each of the pets you sell speak.

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



# Another example for factory pattern

class shapeinterface():
	def draw(self):
		pass

class circle(shapeinterface):
	def draw(self):
		print('Circle ')

class square(shapeinterface):
	def draw(self):
		print('square')


class shapefactory:
	@staticmethod
	def getshape(type):
		if type == 'circle':
			return circle()
		if type == 'square':
			return square()
		raise NotImplementedError('This shape not defined '+ type)


f = shapefactory()
s = f.getshape('circle')
print(s)
s = f.getshape('rect')

# <__main__.circle object at 0x108078f50>
# NotImplementedError: This shape not defined rect