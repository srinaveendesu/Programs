"""
Take a look at what is going on in that example:

1)  generate_power() is a factory function, which simply means
    that it creates a new function each time it is called and
    then returns the newly created function. Thus, raise_two()
    and raise_three() are the newly created functions.

2)  What does this new, inner function do? It takes a single argument,
    power, and returns number**power.

3)  Where does the inner function get the value of number from? This is
    where the closure comes into play: nth_power() gets the value of power
    from the outer function, the factory function. Let’s step through this process:

        Call the outer function: generate_power(2).
        Build nth_power(), which takes a single argument power.
        Take a snapshot of the state of nth_power(), which includes number=2 .
        Pass that snapshot into generate_power().
        Return nth_power().

To put it another way, the closure “initializes” the number bar in
nth_power() and then returns it. Now, whenever you call that newly
returned function, it will always see its own private snapshot that includes power=2.

"""

def generate_power(number):
    # Define the inner function ...
    def nth_power(power):
        return number ** power
    # ... that is returned by the factory function.

    return nth_power


raise_two = generate_power(2)
raise_three = generate_power(3)
print(raise_two(7))

print(raise_three(5))


#####################################
# Decorator implementation of the same

def generate_power(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator


@generate_power(2)
def raise_two(n):
    return n

print(raise_two(7))


@generate_power(3)
def raise_three(n):
    return n

print(raise_three(5))
