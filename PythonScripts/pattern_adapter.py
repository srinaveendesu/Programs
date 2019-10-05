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