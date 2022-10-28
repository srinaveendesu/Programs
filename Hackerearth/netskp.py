# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()


# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab with the + button.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!

# Question
# 1. Define a binary tree structure.
#    Nodes can have a integer as their value
# 2. Write a method to compare two binary trees.
#    Return TRUE if identical, FALSE if different.


from collections import deque


class Node:
    def __init__(self, data, ):
        self.data = data
        self.left = None
        self.right = None


def compare(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 is None and t2 is not None:
        return False

    if t1 is not None and t2 is None:
        return False

    if t1 is not None and t2 is not None:
        if t1.data == t2.data:
            val1 = compare(t1.left, t2.left)
            val2 = compare(t1.right, t2.right)
            if (val1 and val2):
                return True
            else:
                return False


t1 = Node(1)
t2 = Node(1)

t1.left = Node(5)
t2.left = Node(5)

t1.right = Node(6)
t2.right = Node(6)

print(compare(t1, t2))

t1 = Node(1)
t2 = Node(1)

t1.left = Node(5)
t2.left = Node(5)

t1.right = Node(6)
t2.right = Node(7)

print(compare(t1, t2))

t1 = Node(1)
t2 = Node(1)

t1.left = Node(5)
t2.left = Node(5)

t1.right = Node(6)
t2.right = Node(6)

t1.left.right = Node(7)
t2.left.right = Node(7)

t1.right.left = Node(8)
t2.right.left = Node(8)

"""
        1

    5           6

        7   8


        1

    5           6

7           8

"""

print(compare(t1, t2))


def compare_non_recursive(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 is None and t2 is not None:
        return False

    if t1 is not None and t2 is None:
        return False

    lst = deque()
    lst.append([t1, t2])
    while lst:

        n1, n2 = lst.pop()

        if n1.data != n2.data:
            return False

        if n1.left and n2.left:
            lst.append([n1.left, n2.left])
        elif n1.left or n2.left:
            return False

        if n1.right and n2.right:
            lst.append([n1.right, n2.right])
        elif n1.right or n2.right:
            return False

    return True


t1 = Node(1)
t2 = Node(1)

t1.left = Node(5)
t2.left = Node(5)

t1.right = Node(6)
t2.right = Node(6)

print(compare_non_recursive(t1, t2))

t1 = Node(1)
t2 = Node(1)

t1.left = Node(5)
t2.left = Node(5)

t1.right = Node(6)
t2.right = Node(7)

print(compare_non_recursive(t1, t2))
