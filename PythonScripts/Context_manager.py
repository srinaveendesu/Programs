# creating a context manager
# the direct approach
class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "You are in a with block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__:'
                  'normal exit detected.')
        else:
            print('LoggingContextManager.__exit__:'
                  'Exception Detected'
                  'type={}, value={}, traceback={}'.format(exc_type, exc_val, exc_tb))

# Context managers using decorators and generators
# yield is used to achieve the same
# In this we need to explicitly create
# Exception handling
import contextlib
import sys


@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit', sys.exc_info())