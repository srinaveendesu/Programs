from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    def eat(self):
        print('Eating...')

    @abstractmethod
    def num_legs():
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


d = Dog('Bob')
#a = Animal()

d.walk()