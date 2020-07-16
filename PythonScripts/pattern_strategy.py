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

# Example2

# he Strategy pattern allows you to define a family of algorithms, encapsulate each one, and makes them interchangeable.
# It lets the algorithm vary independently from the clients that use it

class PrimeFinder:

    def __init__(self):
        self.primes = []

    def calculate(self, limit):
        """ Will calculate all the primes below limit. """
        pass

    def out(self):
        """ Prints the list of primes prefixed with which algorithm made it """
        print(self.__class__.__name__)
        for prime in self.primes:
            print(prime)


class HardCodedPrimeFinder(PrimeFinder):
    def calculate(self, limit):
        hardcoded_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        primes = []
        for prime in hardcoded_primes:
            if (prime < limit):
                self.primes.append(prime)


class StandardPrimeFinder(PrimeFinder):
    def calculate(self, limit):
        self.primes = [2]
        # check only odd numbers.
        for number in range(3, limit, 2):
            is_prime = True
            for prime in self.primes:
                if (number % prime == 0):
                    is_prime = False
                    break
            if (is_prime):
                self.primes.append(number)


class PrimeFinderClient:

    def __init__(self, limit):
        self.limit = limit
        if limit <= 50:
            self.finder = HardCodedPrimeFinder()
        else:
            self.finder = StandardPrimeFinder()

    def get_primes(self):
        self.finder.calculate(self.limit)
        self.finder.out()

p = PrimeFinderClient(50)
p.get_primes()

p = PrimeFinderClient(65)
p.get_primes()

# HardCodedPrimeFinder
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# StandardPrimeFinder
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61