#!/usr/bin/python
import signal

def signal_hdl(signum, frame):
	print 'signal handler is called with signal ', signum
	sys.stdout.flush()
	sys.exit(0);

adblogcatpid = os.fork()
if adblogcatpid == 0:
	sys.stdout = open('out.txt', 'w')
	signal.signal(signal.SIGUSR1, signal_hdl)
	print 'msg from child'
	time.sleep(20)
else:
	print 'msg from parent'
	time.sleep(1)
	os.kill(adblogcatpid,10)
	os.wait()

sys.exit(0)


