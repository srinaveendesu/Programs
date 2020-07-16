# structural pattern

# Adapter converts the interface of a class into another
# one a client is expecting. This time our problem is that
# the interfaces are incompatible between a client and a server.
# In our scenario, we have Korean and British objects which have
# different method names for speaking. Instead, the client would
# like to use a uniform interface that is the speak method. Our
# solution is the use of the adapter pattern that translates the
# method names in between the client and the server code.
#
#
# Bridges and decorators are related to the adapter pattern.

class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        # For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))

# Korean says 'An-neyong?'
#
# British says 'Hello!'


# Example 2

# The adapter converts the interface of a class into another interface that clients expect.
# It lets classes work together that couldn't otherwise, because of incompatible interfaces

# Adaptee (source) interface
class EuropeanSocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass

# Target interface
class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass

# Adaptee
class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

# Client
class AmericanKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")

class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()

socket = EuropeanSocket()
kettle = AmericanKettle(socket)
kettle.boil()

adapter = Adapter(socket)
kettle = AmericanKettle(adapter)
kettle.boil()

# Kettle on fire!
# Coffee time!