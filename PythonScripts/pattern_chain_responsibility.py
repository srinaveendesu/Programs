# Behavioral Pattern

# Chain of Responsibility opens up various possibilities of
# processing for a given request. The Chain of Responsibility
# pattern decouples the request and its processing. Our given
# problem is that many different types of processing needs to
# be done depending on what the request is. In our scenario, we
# receive an integer value and then we use different handlers to
# find out its range. As our solution, we used Abstract Handler
# that stores a Successor who will handle a request if it is not
# handled at the current handler. then Concrete Handlers check if
# they can handle the request. If they can, they handle it and return
# a true value indicating that the request was handled.


# Composite is related to the Chain of Responsibility design pattern.

class Handler: #Abstract handler
	"""Abstract Handler"""
	def __init__(self, successor):
		self._successor = successor # Define who is the next handler

	def handle(self, request):
			handled = self._handle(request) #If handled, stop here

			#Otherwise, keep going
			if not handled:
				self._successor.handle(request)

	def _handle(self, request):
		raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): # Inherits from the abstract handler
	"""Concrete handler 1"""
	def _handle(self, request):
		if 0 < request <= 10: # Provide a condition for handling
			print("Request {} handled in handler 1".format(request))
			return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from the abstract handler
	"""Default handler"""

	def _handle(self, request):
		"""If there is no handler available"""
		#No condition checking since this is a default handler
		print("End of chain, no handler for {}".format(request))
		return True # Indicates that the request has been handled

class Client: # Using handlers
	def __init__(self):
		self.handler = ConcreteHandler1(DefaultHandler(None)) # Create handlers and use them in a sequence you want
		                                                      # Note that the default handler has no successor

	def delegate(self, requests): # Send your requests one at a time for handlers to handle
		for request in requests:
				self.handler.handle(request)

# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)


# Request 2 handled in handler 1
# Request 5 handled in handler 1
# End of chain, no handler for 30

# Example 2

# he Chain of Responsibility pattern avoids coupling the sender of a request to the receiver,
# by giving more than one object a chance to handle that request

class Car:
	def __init__(self, name, water, fuel, oil):
		self.name = name
		self.water = water
		self.fuel = fuel
		self.oil = oil

	def is_fine(self):
		if self.water >= 20 and self.fuel >= 5 and self.oil >= 10:
			print('Car is good to go')
			return True
		else:
			return False


class Handler:
	def __init__(self, successor=None):
		self._successor = successor

	def handle_request(self, car):
		if not car.is_fine() and self._successor is not None:
			self._successor.handle_request(car)


class WaterHandler(Handler):

	def handle_request(self, car):
		if car.water < 20:
			car.water = 100
			print('Added water')
		super().handle_request(car)


class FuelHandler(Handler):

	def handle_request(self, car):
		if car.fuel < 5:
			car.fuel = 100
			print('Added fuel')
		super().handle_request(car)


class OilHandler(Handler):

	def handle_request(self, car):
		if car.oil < 10:
			car.oil = 100
			print('Added oil')
		super().handle_request(car)


garage_handler = OilHandler(FuelHandler(WaterHandler()))
car = Car('mycar',1,1,1)
garage_handler.handle_request(car)
car = Car('mycar',5,5,5)
garage_handler.handle_request(car)
car = Car('mycar',10,10,10)
garage_handler.handle_request(car)

# Added oil
# Added fuel
# Added water
# Car is good to go
# Added oil
# Added water
# Car is good to go
# Added water
# Car is good to go
