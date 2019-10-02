# Structural Pattern

# Adding new features to existing object dynamically
# and not using subclassing

# Use functions acitng as objects in python feature

# patterns such as adapter,composite and strategy are related to this pattern

from functools import wraps

def make_blink(function):
	"""Defines the decorator"""

	#This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	#Define the inner function
	def decorator():
		#Grab the return value of the function being decorated
		ret = function()

		#Add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>"

	return decorator

#Apply the decorator here!
@make_blink
def hello_world():
	"""Original function! """

	return "Hello, World!"

#Check the result of decorating
print(hello_world())

#Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

#Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)


# <blink>Hello, World!</blink>
# hello_world
# Original function!
