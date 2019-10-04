# Creational Pattern

# Builder is a solution to an Anti-Pattern called Telescoping Constructor.
# An Anti-Pattern is the opposite of the best practice. The Telescoping Constructor
# Anti-Pattern occurs when a software developer attempts to build a complex object
# using an excessive number of constructors. The Builder pattern is trying to
# solve this problem. Think of a scenario, in which you're trying to build a car.
# This requires various car parts to be first constructed individually and then assembled.
# The Builder pattern brings an order to this chaotic process to remove this unnecessary
# complexity in building a complex object. The Builder partitions the process of building
# a complex object into the four different roles. The first role is Director, and Director
# is in charge of actually building a product using the builder object. Then, the builder
# class provides all the necessary interfaces required in building an object. We call this
# an Abstract Builder, because there will be a Concrete Builder inheriting from this Abstract
# Builder. The Concrete Builder class inherits from the Builder class and actually implements
# the details of the interfaces of the Builder class, for a specific type of a product. And
# the product represents an object being built. The Builder Pattern does not rely on polymorphism,
# unlike Factory and Abstract Factory. The focus of the Builder Pattern is rather on reducing
# the complexity of building a complex object through a divide and conquer strategy.


class Director():

    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """

    def add_model(self):
        self.car.model = "Audi"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)

# Audi | Regular tires | Turbo engine