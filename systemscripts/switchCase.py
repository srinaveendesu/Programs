#!/usr/bin/python
		
''' There is no switch or case in Python ... because you can
do better by using its OO capabilities and a dictionary. '''

def errhandler (): print 'Your input has not been recognised'
def doblue (): print 'The sea is blue'
def dogreen (): print 'Grass is green'
def doyellow (): print 'Sand is yellow'
def redflag ():
   print 'Red is the colour of fire'
   print 'do NOT play with fire'


# set up a dictionary of actions

takeaction = {
	'blue': doblue,
	'green': dogreen,
	'yellow': doyellow,
	'red': redflag
	}

colour = raw_input('Please enter red blue green or yellow ')
takeaction.get(colour,errhandler)()

# Uses the get method to allow us to specify a default
