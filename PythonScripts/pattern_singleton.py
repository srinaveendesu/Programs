# Creational Pattern

# An object-oriented way of providing global variables is Singleton.
# Singleton is the pattern you need when you'd like to allow only
# one object to be instantiated from a class. Like I said, creating
# a global variable in an object-oriented way is Singleton. Why would
# you need such a pattern? Let's say that there is a need for keeping
# a cache of information to be shared by various elements of your software
# system. By keeping this information in the single object, there's no need
# to retrieve the information from its original source every time. So in this case,
# Singleton acts as a cache of the information. Modules in Python act as Singletons.
#
# There are also a number of ways of implementing Singleton,
# but we'll be using the Borg design pattern to implement our Singleton.

class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""

    # This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary for printing


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)

print(x)

# {'HTTP': 'Hyper Text Transfer Protocol'}
# {'HTTP': 'Hyper Text Transfer Protocol', 'SNMP': 'Simple Network Management Protocol'}
# {'HTTP': 'Hyper Text Transfer Protocol', 'SNMP': 'Simple Network Management Protocol'}