import logging
import threading
import time


def worker(num):
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')
    print("Worker: %s" % num)

def my_service():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')
    print("some bullshit")


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)


t = threading.Thread(name='my_service', target=my_service, daemon=True)
w = threading.Thread(name='worker', target=worker, args=(5,))
w2 = threading.Thread(target=worker, args=(10,)) # use default name

w.start()
w2.start()
t.start()
#java applications ont.join(4)
print('t.isAlive()', t.isAlive())
print("Adios")
