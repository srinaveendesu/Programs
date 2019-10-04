# Creational Pattern

# Prototype clones objects according to a prototypical instance.
# Prototype is especially useful when creating many identical objects
# individually. So this could be very expensive. And cloning could be
# a good alternative instead of creating individual objects one at a time.
# Let's assume that we are building a car. We can mass produce cars if
# the cars have the same color and the same options. So in this case,
# you can simply clone the objects instead of creating the individual
# objects one at a time. So the solution in this case consists of creating
# a prototypical instance first and then simply cloning it whenever
# you need a replica.
#
# One of the patterns related to the prototype pattern is abstract factory.

import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Benz"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('Benz', c)

c1 = prototype.clone('Benz')

print(c1)

# Benz | Red | Ex