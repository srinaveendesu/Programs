from time import time
from contextlib import contextmanager

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"


@contextmanager
def new_log_file(name):
    try:
        logname = name
        f = open(logname, 'w')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print ("logfile created")
        f.close()


# with new_log_file('dump') as f:
#     f.write('this is the body')
#
# A new file will be created (dump file)
#
# This is the header
# tnis is the body
# this is the footer