from multiprocessing import Process
import time

####### SINGLE PROCESS

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO PROCESSES


# With two processes, we can do them both at once...
process = Process(target=complex_calculation)
process.start()

start = time.time()

ask_user()

process.join()  # this waits for the process to finish

print('Two process total time: ', time.time() - start)

# Run this and see what happens!

# Process Pools
from concurrent.futures import ProcessPoolExecutor

####### TWO PROCESSES


# With two processes, we can do them both at once...
start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(complex_calculation)

print('Two process total time: ', time.time() - start)

# Run this and see what happens!


# Enter your name: a
# Hello, a
# ask_user:  3.3599350452423096
# Started calculating...
# complex_calculation:  4.805688142776489
# Single thread total time:  8.16568112373352
#
#
# Enter your name: Started calculating...
# a
# Hello, a
# ask_user:  2.0295188426971436
# complex_calculation:  4.769603729248047
# Two process total time:  4.773864984512329
# Started calculating...
# Started calculating...
# complex_calculation:  4.9664881229400635
# complex_calculation:  4.981385946273804
# Two process total time:  4.990784168243408
