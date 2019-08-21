# Simple generators in synchronised multitasking

print('####### Simple Generator########')
def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')


# A two way implemented generators

print ('############Two way Generators############')
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass


friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
print(next(g))

# Generator receiving through yield

print ('#########enerator receiving through yield#############')
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')


# ####### Simple Generator########
# 10
# 5
# 20
# 9
# 4
# 19
# 8
# 3
# 18
# 7
# 2
# 17
# 6
# 1
# 16
# 5
# Task finished
# 15
# 4
# 14
# 3
# 13
# 2
# 12
# 1
# 11
# Task finished
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Task finished
# ############Two way Generators############
# HELLO Rolf
# HELLO Jose
# #########enerator receiving through yield#############
# Hello ROLF
# Hello, world! Multitasking...
# How are you, JOSE