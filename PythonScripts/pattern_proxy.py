# Structural Pattern

# Proxy becomes handy when creating an object that is very
# resource intensive. The problem we need to solve here is to
# postpone our object creation as long as possible, due to the
# resource intensive nature of the object we're creating. Therefore,
# there is a need for a placeholder which will in turn create the
# object if its creation is absolutely necessary. So here is our scenario.
# So in our scenario, we create this instance of the Producer class
# only when he's available, because only a fixed number of Producer
# objects can exist at a given time. Our Proxy in this case is an artist
# who is checking to see if the Producer becomes available for a guest.
# In the Proxy design pattern clients interact with a Proxy object most
# of the time until the resource intensive object becomes available.
# Therefore, the Proxy object is in charge of creating the resource intensive objects.
#
#
# Adapter and Decorator are related to the Proxy design pattern.

import time


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """"Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available ...")

        if self.occupied == 'No':
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # Make the prodcuer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = 'Yes'

# Make the Producer produce
p.produce()



# Artist checking if Producer is available ...
# Producer has time to meet you now!
# Artist checking if Producer is available ...
# Producer is busy!


# Example 2

# A proxy provides a surrogate or place holder to provide access to an object

# why
# use an extra level of indirection to support distributed, controlled or conditional access
# add a wrapper and delgation to protect the real component from undue complexity

class SubjectInterface:
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """
    def request(self): pass


class Proxy(SubjectInterface):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy may be doing something, like controlling request access")
        self._real_subject.request()


class RealSubject(SubjectInterface):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        print("The real thing is dealing with the request")


rs = RealSubject()
rs.request()
p = Proxy(rs)
p.request()

# The real thing is dealing with the request
# Proxy may be doing something, like controlling request access
# The real thing is dealing with the request

# example 3

class Blog:
    def read(self):
        print('Read the blog')

    def write(self):
        print('Write the blog')

class Proxy:
    def __init__(self, target):
        self.target = target

    def __getattr__(self, attr):
        return getattr(self.target, attr)

class AnonUserBlogProxy(Proxy):
    def __init__(self, blog):
        super().__init__(blog)
    def write(self):
        print('Only authorized users can write blog posts.')


b = Blog()
b.write()
p = AnonUserBlogProxy(b)
p.write()

# Write the blog
# Only authorized users can write blog posts.