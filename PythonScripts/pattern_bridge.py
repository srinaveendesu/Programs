# Structural Pattern

# The bridge pattern helps untangle an unnecessary complicated
# class hierarchy, especially when implementation specific classes
# are mixed together with implementation-independent classes. So our
# problem here is that there are two parallel or orthogonal abstractions.
# One is implementation-specific, and the other one is implementation-independent.
# And our scenario involves this implementation-independent circle abstraction
# and implementation-dependent circle abstraction. The implementation-dependent
# circle abstraction involves how to draw a circle, and implementation-independent
# circle abstraction involves how to define the properties of a circle and scale it.
# The key to our solution is not trying to abstract both implementation-specific and
# implementation-independent classes in a single class hierarchy.


# The abstract factory and adaptor patterns are the related patterns to this rich design pattern.


class DrawingAPIOne(object):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
	"""Implementation-specific abstraction: concrete class two"""
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class Circle(object):
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		"""Implementation-independent"""
		self._radius *= percent


#Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
#Draw a circle
circle2.draw()


# API 1 drawing a circle at (1, 2 with radius 3!)
# API 2 drawing a circle at (2, 3 with radius 4!)