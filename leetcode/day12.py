#https://leetcode.com/problems/min-stack/submissions/
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

class MinStack:

    def __init__(self):

        self.Stack = []
        self.minVal = None

    def push(self, val: int) -> None:

        if not self.Stack or self.minVal == None:
            self.minVal = val

        if not self.Stack:
            self.Stack.append(val)
        elif val < self.minVal:
            self.Stack.append(2 * val - self.minVal)
            self.minVal = val
        else:
            self.Stack.append(val)

    def pop(self) -> None:

        if not self.Stack:
            return
        elif self.Stack[-1] < self.minVal:
            self.minVal = 2 * self.minVal - self.Stack[-1]
            self.Stack.pop()
        else:
            self.Stack.pop()

    def top(self) -> int:

        if self.Stack[-1] > self.minVal:
            return self.Stack[-1]
        else:
            return self.minVal

    def getMin(self) -> int:

        return self.minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# https://leetcode.com/problems/combine-two-tables/solution/

# Write your MySQL query statement below


# select
# Person.FirstName, Person.LastName, Address.City, Address.State
# from Person
#
# LEFT
# JOIN
# Address
# ON
# Address.PersonId = Person.PersonID