import time
from functools import wraps


def timer(func):
    """
    decorator function to time a def

    prints to standar output human readable time measure
    e.g. 
    Completed def_function_name in: 1 weeks, 4 days, 8 hours, 13 minutes, 21.123123 seconds
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        formatted_time = time_formatter(run_time)
        print(f"Task {func.__name__} completed  in: {formatted_time}")
        return value
    return wrapper


time_intervals = (
    ('weeks', 604800),
    ('days', 86400),
    ('hours', 3600),
    ('minutes', 60),
)


def time_formatter(seconds):
    formatted_time = ''
    if seconds < 60:
        return f"{seconds:.6f} seconds"
    for unit, count in time_intervals:
        value = seconds // count
        if value:
            remainder = seconds - count * value
            formatted_time = formatted_time + time_formatter(remainder)
            return f"{int(value)} {unit}, " + formatted_time
