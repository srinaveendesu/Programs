# Behavioral Pattern

# The Strategy pattern offers a family of interchangeable
# algorithms to a client. The problem we often see is that
# there is a need for dynamically changing the behavior of an
# object. So we offer our Strategy class with its default behavior.
# When there is a need, we provide another variation of the Strategy
# class by dynamically replacing its default method with a new one.
# Python allows adding methods dynamically by importing the types module.


import types  # Import the types module


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()


# Default Strategy is used!
# Strategy One is used to execute method 1
# Strategy Two is used to execute method 2