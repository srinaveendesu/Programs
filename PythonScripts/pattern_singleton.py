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


# Singleton pattern ensures that a class have only one instance and provide a global point of access to it
# borg idiom( a.k.a monostate pattern) lets a class have as many instances as one likes, but ensures
# that they all share the same state

# __new__ is the first step of instance create; its called before __init__ and
# is responsible for returning a new instance of your class

# __init__ doesnt return ianything; responsible for intializing the instance after its been created

class Singleton:
    __instance = None
    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

s  = Singleton()
s.val = 'foo'
print(s.val)
y = Singleton()
y.val = 'boo'
print(y.val)
print(s.val)
print(s is y )
# foo
# boo
# boo
# True

b = Borg()
c = Borg()
print(b is c)
b.val = "doo"
c.val = "coo "
print(b.val ,c.val)
# False
# coo  coo

# python modules are singletons
