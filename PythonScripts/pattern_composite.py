# Structural Pattern

# The composite design pattern maintains a tree data structure
# to represent part-whole relationships. Here we like to build
# a recursive tree data structure so that an element of the tree
# can have its own sub-elements. An example of this problem is
# creating menu and submenu items. The submenu items can have
# their own sub-submenu items. So our coding challenge is to
# display menu and submenu items using this composite design pattern.
# Our solution consists of three major elements. The first one is
# component, the second one is child, and the third one is composite.
# The component element is an abstract class. A concrete class called
# child inherits from this component class. And then we have another
# concrete class called composite, which is also inheriting from the
# component class. Finally, our composite class maintains child objects
# by adding and removing them to a tree data structure.
#
#
# Decorator, iterator, and visitor are related to the composite design pattern.

class Component(object):
	"""Abstract class"""

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component): #Inherits from the abstract class, Component
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of your child item!
		self.name = args[0]

	def component_function(self):
		#Print the name of your child item here!
		print("{}".format(self.name))

class Composite(Component): #Inherits from the abstract class, Component
	"""Concrete class and maintains the tree recursive structure"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of the composite object
		self.name = args[0]

		#This is where we keep our child items
		self.children = []

	def append_child(self, child):
		"""Method to add a new child item"""
		self.children.append(child)

	def remove_child(self, child):
		"""Method to remove a child item"""
		self.children.remove(child)

	def component_function(self):

		#Print the name of the composite object
		print("{}".format(self.name))

		#Iterate through the child objects and invoke their component function printing their names
		for i in self.children:
			i.component_function()

#Build a composite submenu 1
sub1 = Composite("submenu1")

#Create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")
#Create a new Child sub_submenu 12
sub12 = Child("sub_submenu 12")

#Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
#Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

#Build a top-level composite menu
top = Composite("top_menu")

#Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

#Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

#Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

#Let's test if our Composite pattern works!
top.component_function()


# top_menu
# submenu1
# sub_submenu 11
# sub_submenu 12
# submenu2