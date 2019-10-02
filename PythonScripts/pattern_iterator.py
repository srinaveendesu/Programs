# Behavioral Pattern

# The iterator pattern allows a client to have sequential access
# to the elements of an aggregate object without exposing its
# underlying structure. The problem is that some programmers overcrowd
# the traversal interfaces of an aggregate object for every possible
# way of iteration. We'll be building our own iterator that takes advantage
# of a built-in Python iterator called zip(). The iterator iterates through
# a list of German counting words. It will iterate only up to a certain
# point based on a client input. An iterator isolates access and traversal
# features from an aggregate object. It also provides an interface for accessing
# the elements of an aggregate object. An iterator keeps track of the
# objects being traversed. One of the recommended solutions is to make the
# aggregate object create an iterator for a client.


# The composite design pattern is related to the iterator pattern.

def count_to(count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number

    # Let's test the generator returned by our iterator


for num in count_to(3):
    print("{}".format(num))

# eins
# zwei
# drei

for num in count_to(4):
    print("{}".format(num))


# eins
# zwei
# drei
# vier
