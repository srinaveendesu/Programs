# Creational Pattern

# Abstract Factory is especially useful when a client expects to
# receive a family of related objects at a given time, but don't
# have to know which family it is until run time. Here is the
# scenario we'll be using. We'll first build a pet factory whose
# concrete factories include Dog factory and Cat factory. Both dog
# and cat factories produce related products such as dog food and
# cat food. At least in theory our solution, Abstract Factory,
# consists of Abstract factory, Concrete factory, Abstract product,
# and Concrete product. For the Abstract factory we use pet factory
# in our example. For concrete factory we use dog factory and cat
# factory in our example. And finally for the concrete product we'll
# be creating the dog, which is a pet, and the dog food, and also cat
# and the cat food.
#
# We implement our Abstract Factory without using inheritance, mainly
# because Python is a dynamically typed language and therefore does
# not require abstract classes.
#
#
# Abstract Factory is related to factory method and the concrete factories are often singletons.

class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Dog Food!"


class PetStore:
	""" PetStore houses our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """

		self._pet_factory = pet_factory


	def show_pet(self):
		""" Utility method to display the details of the objects retured by the DogFactory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


#Create a Concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()

# Our pet is 'Dog'!
# Our pet says hello by 'Woof!'
# Its food is 'Dog Food!'!

# Example 2

# provide an interface for creating a families of realted objects without specifying their concrete class

# create the family of interfaces or abstract base classes
# create the concrete classes for each of these
# create an abstract factory which applies to the whole family
# create a concrete factory for each base class

# abstract base class

class shape2dinterface:
	def draw(self):
		pass

class shape3dinterface:
	def build(self):
		pass

# concrete class

class circle(shape2dinterface):
	def draw(self):
		print('circle')

class square(shape2dinterface):
	def draw(self):
		print('cube')

class shpere(shape3dinterface):
	def build(self):
		print('sphare')

class cube(shape3dinterface):
	def build(self):
		print('cube')

# Abstract factory class

class shapefactoryinterface:
	def getshape(sides):
		pass

# concrete shape factores

class shape2dfactory(shapefactoryinterface):
	@staticmethod
	def getshape(sides):
		if sides == 1:
			return circle()
		if sides == 4:
			return square()
		raise NotImplementedError('sides not exist' + sides)

class shape3dfactory(shapefactoryinterface):
	@staticmethod
	def getshape(faces):
		if faces == 1:
			return shpere()
		if faces == 6:
			return cube()
		raise NotImplementedError('sides not exist' + faces)


s = shape2dfactory()
s.getshape(1).draw()

s = shape3dfactory()
s.getshape(6).build()

# circle
# cube