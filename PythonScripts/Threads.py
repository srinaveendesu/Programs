import time
from threading import Thread

####### SINGLE THREAD

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
# Single thread total time:  10.554189920425415 

####### TWO THREADS

# This execution demonstrates how an I/O operation can be
# time decreased. While one thread processes for computing
# another thread does the I/O operation
# With two threads, we can do them both at once...
thread = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread.start()
thread2.start()

thread.join()
thread2.join()

print('Two thread total time: ', time.time() - start)
# Two thread total time:  8.154620170593262

# Run this and see what happens!

# The following demo describes how python is a single threaded application
# Two threads do not run in parallel.

thread3 = Thread(target=complex_calculation)
thread4 = Thread(target=complex_calculation)

start = time.time()

thread3.start()
thread4.start()

thread3.join()
thread4.join()

print('\nTwo computation thread total time: ', time.time() - start)

# Two computation thread total time:  16.565603494644165

# Thread Pool example


from concurrent.futures import ThreadPoolExecutor

####### TWO THREADS


# With two threads, we can do them both at once...
start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(ask_user)

# All this does is we don't have to call pool.shutdown()

print('ThreadPool: Two thread total time: ', time.time() - start)
# ThreadPool: Two thread total time:  7.850630283355713