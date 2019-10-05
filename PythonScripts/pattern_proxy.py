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