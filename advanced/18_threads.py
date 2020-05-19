"""Python threads."""

import threading
import time
import concurrent.futures
import random
import datetime


def do_threading(some_string, some_integer):
    print("in do_threading")
    print("some_string =", some_string)
    print("some_integer =", some_integer)
    time.sleep(some_integer)
    print("do_threading exiting...")


print("\ncreate a thread...")
my_thread = threading.Thread(target=do_threading, args=('some arguments', 1))   # use 'daemon=True' to create daemon...
print("start thread")                                                           # background process which will
my_thread.start()                                                               # terminate when program finishes
print("returned from start, wait for the thread to complete using join()")
my_thread.join()
print("returned from join")


class MyThread(threading.Thread):
    def __init__(self):
        self.main_lock = threading.Lock()
        self.continue_processing = True
        super().__init__()

    def get_continue_processing(self):
        with self.main_lock:
            return self.continue_processing

    def stop_processing(self):
        with self.main_lock:
            self.continue_processing = False

    def run(self):
        while self.get_continue_processing():
            print("MyThread::run: still working")
            time.sleep(0.5)
        print("MyThread::run: stopped working")


print("\nusing a threaded class...")
my_threaded_class = MyThread()
print("start the threaded class")
my_threaded_class.start()
print("go away and do lots of crazy stuff")
time.sleep(3)
print("ok that's all done, don't need that thread any more")
my_threaded_class.stop_processing()
print("back from stop_processing")
time.sleep(2)           # let MyThread stop before doing anything else


print("\nusing a thread pool executor for launching multiple threads...")


def do_some_stuff():
    time.sleep(3)
    print("done some stuff")
    return 'do_some_stuff return value'


def do_some_other_stuff():
    time.sleep(1)
    print("done some other stuff")
    return 'do_some_other_stuff return value'


executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
print("submit do_some_stuff")
stuff_future_object = executor.submit(do_some_stuff)
print("submit do_some_other_stuff")
other_future_object = executor.submit(do_some_other_stuff)
print(stuff_future_object)
print(other_future_object)
print("wait for threads to complete")
for f in concurrent.futures.as_completed([stuff_future_object, other_future_object]):
    print(f)
    print("result from this thread =", f.result())


def my_worker_thread(my_string):
    print("starting worker thread to calculate length of", my_string)
    if my_string == 'bob':
        time.sleep(3)
    return f"length of {my_string} is {len(my_string)}"


print("\nusing map to launch multiple worker threads...")
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    map_results = executor.map(my_worker_thread, ['bob', 'denise', 'reginald', 'sidney'])
    for result in map_results:       # will have to wait for 'bob' to finish as results provided in order given
        print(result)

print("\nor as an alternative...")
# https://stackoverflow.com/questions/20838162/how-does-threadpoolexecutor-map-differ-from-threadpoolexecutor-submit
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # use list comprehension, no need for map
    mapped_futures = [executor.submit(my_worker_thread, x) for x in ['bob', 'denise', 'reginald', 'sidney']]
    for f in concurrent.futures.as_completed(mapped_futures):   # get results in order of completion
        print(f.result())


def my_greedy_worker_thread(name, a_semaphore):
    print(f"thread {name} has started!")
    a_semaphore.acquire()
    print(f"thread {name} acquired semaphore for resource!")
    time.sleep(random.randint(1, 3))
    print(f"thread {name} finished with resource so releasing!")
    a_semaphore.release()
    return f'thread {name} is done'


print("\nsemaphores are usually shared between threads as a way to control resources...")
my_semaphore = threading.Semaphore(2)       # 2 resources

print("starting thread pool with 5 threads and 2 resources")
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # use list comprehension, no need for map
    my_futures = [executor.submit(my_greedy_worker_thread, x, my_semaphore) for x in range(5)]
    for f in concurrent.futures.as_completed(my_futures):   # get results in order of completion
        print(f.result())


def wait_for_an_event(event, number_events):
    events_detected = 0
    while events_detected < number_events:
        print("waiting for event")
        event.wait()                    # you can specify a timeout here e.g. wait(timeout=0.5) for 500ms wait
        print("got event")
        event.clear()                   # need to clear events
        events_detected += 1
    print("all events detected, thread terminating...")


my_event = threading.Event()

print("\nusing events to signal other threads...")
my_thread = threading.Thread(name='wait_for_an_event', target=wait_for_an_event, args=(my_event, 5))
print("starting thread")
my_thread.start()
for i in range(5):
    time.sleep(0.5)
    print("set event")
    my_event.set()
my_thread.join()


def my_function(a_string):
    print(a_string)


print("\nusing timers to run a function at some future point in time...")
timer_thread = threading.Timer(2, my_function,args=("time's up!",))
timer_thread.start()
print("timer_thread=", timer_thread)
timer_thread.join()   # might as well wait in this demo but obviously you might do something interesting here, or not
print("timer_thread=", timer_thread)


def thread_a(a_barrier):
    print("thread_a started at", datetime.datetime.now())
    time.sleep(2)       # do something that needs to be done for both threads before go any further e.g. client/server
    a_barrier.wait()
    print("thread_a: ok all in sync now, we can start...")
    # do something exciting....
    return f"thread_a: time = {datetime.datetime.now()}"


def thread_b(a_barrier):
    print("thread_b started at", datetime.datetime.now())
    a_barrier.wait()
    print("thread_b: ok all in sync now, we can start...")
    # do something exciting....
    return f"thread_b: time = {datetime.datetime.now()}"


print("\nusing barriers to ensure threads sync up where necessary...")
my_barrier = threading.Barrier(2)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    my_futures = [executor.submit(f, my_barrier) for f in [thread_a, thread_b]]
    for f in concurrent.futures.as_completed(my_futures):
        print(f.result())


def thread_a(a_condition):
    print("thread_a started at", datetime.datetime.now())
    with a_condition:
        print("thread_a: creating the shared resource")
        time.sleep(2)           # let's create a shared resource
        print("thread_a: resource now available, notify everyone")
        a_condition.notify_all()    # notify others shared resource is available
        print("thread_a: others now notified")
    # do something exciting....
    return f"thread_a: time = {datetime.datetime.now()}"


def thread_b(a_condition):
    print("thread_b started at", datetime.datetime.now())
    with a_condition:
        print("thread_b: waiting for shared resource")
        a_condition.wait()
        print("thread_b: we can now use shared resource")
        # do something exciting....
    return f"thread_b: time = {datetime.datetime.now()}"


def thread_c(a_condition):
    print("thread_c started at", datetime.datetime.now())
    with a_condition:
        print("thread_c: waiting for shared resource")
        a_condition.wait()
        print("thread_c: we can now use shared resource")
        # do something exciting....
    return f"thread_c: time = {datetime.datetime.now()}"


print("\nusing conditionals to let other threads know when they can start...")
my_condition = threading.Condition()
my_notifier_thread = threading.Thread(target=thread_a, args=(my_condition,))
consumer_thread_b = threading.Thread(target=thread_b, args=(my_condition,))
consumer_thread_c = threading.Thread(target=thread_c, args=(my_condition,))

consumer_thread_b.start()
time.sleep(1)
consumer_thread_c.start()
time.sleep(1)
my_notifier_thread.start()
