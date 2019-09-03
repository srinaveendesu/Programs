"""
So what in the heck is an iterable?

Funny you’d ask! An iterable is an object that has an `__iter__` method defined. The `__iter__` method *must return an iterator*.

Here’s an example of using our generator to make an iterable.
"""

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

"""
Now we have an iterable which uses the iterator to get the next value of the sequence it generates. We can do this:
"""

print(sum(FirstHundredIterable()))  # gives 4950

for i in FirstHundredIterable():
    print(i)

"""
Wait… I remember something about for loops. We needed an object with `__len__` and `__getitem__` defined!

How come we can use a for loop with this object that doesn’t have either of those?

Here’s something new! You can perform iteration over an iterable. An iterable either has:

* `__len__` and `__getitem__` defined; or
* An `__iter__` method that returns an iterator.

If you have either of those two, you have yourself an iterable.

---

So the `FirstHundredIterable` is returning an object of type `FirstHundredGenerator`. 

Inside `FirstHundredGenerator`, what is `self`?

(Hint: it’s an object, what is it’s type?)

(Hint hint: it’s of type `FirstHundredGenerator`).

Knowing that, we can change the generator to this:
"""

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

"""
And then we don’t need a separate iterable at all—the generator itself is now both an iterator and an iterable.
"""

# 4950
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
# 58
# 59
# 60
# 61
# 62
# 63
# 64
# 65
# 66
# 67
# 68
# 69
# 70
# 71
# 72
# 73
# 74
# 75
# 76
# 77
# 78
# 79
# 80
# 81
# 82
# 83
# 84
# 85
# 86
# 87
# 88
# 89
# 90
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 98
# 99