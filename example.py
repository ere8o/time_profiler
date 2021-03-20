from time import sleep
from time_profiler import timer

@timer
def wait_x_seconds(seconds):
    sleep(seconds)
    pass

wait_x_seconds(3)
