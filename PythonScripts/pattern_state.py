# behavioral pattern

# the State pattern allows an object to alter its behavior when its internal state changes.

# Base state class
class ComputerState:
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print ('Current:', self ,' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self ,' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name

class Off(ComputerState):
    name = "off"
    allowed = ['on']

class On(ComputerState):
    name = "on"
    allowed = ['off','suspend','hibernate']

class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']

class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ['on']

class Computer:
    def __init__(self):
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


c= Computer()
print(c.state.__str__())
c.change(On)
c.change(Suspend)
c.change(Hibernate)
c.change(On)
c.change(Off)

# off
# Current: off  => switched to new state on
# Current: on  => switched to new state suspend
# Current: suspend  => switching to hibernate not possible.
# Current: suspend  => switched to new state on
# Current: on  => switched to new state off