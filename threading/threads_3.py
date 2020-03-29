import threading
import time
import logging


def expl_one():
    n = 0

    while n < 7:
        time.sleep(1)
        logging.debug('expl_one here...')
        n = n + 1

def expl_two():
    n = 0

    while n < 5:
        time.sleep(2)
        logging.debug('ja ja ja there')
        n = n + 1

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t1 = threading.Thread(name='Example 1', target=expl_one, daemon=False)
t1.start()
t2 = threading.Thread(name='Example 2', target=expl_two, daemon=False)
t2.start()

print("Main thread has finished already!!")