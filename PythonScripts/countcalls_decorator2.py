# Function decorator for counting number of calls
# Function DECORATOR EXAMPLE

import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()
print (say_whee.num_calls)

# Call 1 of 'say_whee'
# Whee!
# Call 2 of 'say_whee'
# Whee!
# 2