# Structural Pattern

# Python makes implementing Decorator very straightforward due
# to its built in language features. Our challenge here is to
# add additional features to an existing object dynamically
# without using subclassing. Here's our scenario. We start with
# a function simply displaying a Hello World! message, and then
# we'd like to make the message look fancier by decorating it with
# additional tags, such as blink, as you can see here. Functions are
# also objects in Python, and we can simply add additional features
# to these functions using this built in decorator feature in Python.
#
#
# Patterns such as adapter, composite, and strategy are related to the decorator pattern.

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
