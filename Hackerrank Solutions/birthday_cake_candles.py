class Command:
    def execute(self): pass

class test1(Command):
    def execute(self):
        print("You're in  test1.")

class test2(Command):
    def execute(self):
        print("You are in test2")

class test3(Command):
    def execute(self):
        print("you are in test3")

# An object that holds commands:
class processor:
    def __init__(self):
        self.commands = []
    def add(self, command):
        self.commands.append(command)
    def run(self):
        for c in self.commands:
            c.execute()

processor = processor()
processor.add(test1())
processor.add(test2())
processor.add(test3())
processor.run()
