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


# Example 2

# specify the kinds of objects to use a prototypical instance and create new objects by
# copying this prototype

from copy import deepcopy

class Car:
    def __init__(self):
        self.__wheels  = list()
        self.__engine  = None
        self.__body    = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)

    def clone(self):
        return deepcopy(self)

# === Car parts ===
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car


class BuilderInterface:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass


class JeepBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


class NissanBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def getBody(self):
        body = Body()
        body.shape = "hatchback"
        return body

d = Director()
d.setBuilder(JeepBuilder())
jeep = d.getCar()
print(jeep)
print(jeep.specification())
jeep2 = jeep.clone()
print(jeep2)
print(jeep2.specification())

# <__main__.Car object at 0x10166e590>
# body: SUV
# engine horsepower: 400
# tire size: 22'
# None
# <__main__.Car object at 0x10166e9d0>
# body: SUV
# engine horsepower: 400
# tire size: 22'
# None


# Example 3

from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj

p = Point(0,0)
p.__str__()
p1 = p.clone(1,1)
p1.__str__()

# (0, 0)
# (1, 1)