import pytest
import threading
import time
from random import randrange


def thread_function(name, delay):
    print(f"\nThread {name}: starting with delay {delay}")
    time.sleep(delay)
    print(f"\nThread {name}: finishing")


@pytest.mark.parametrize("num_threads, delay", [(3, randrange(4)), (4, randrange(4)), (5, randrange(4))],
                         ids=["3 Threads", "4 Threads", "5 Threads"])
@pytest.mark.sanity_tests
def test_happy_flow(num_threads, delay):
    threads = list()
    for index in range(num_threads):
        print(f"\nMain    : create and start thread {index}.")
        x = threading.Thread(target=thread_function, args=(index, delay, ))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print(f"\nMain    : before joining thread {index}.")
        thread.join()
        print(f"\nMain    : thread {index} done")
