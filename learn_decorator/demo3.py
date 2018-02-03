"""
"""
import datetime
import time
from functools import wraps


def count_runtime(func):
    @wraps(func)
    def with_runtime(*args, **kwargs):
        starttime = datetime.datetime.now()
        out_func = func(*args, **kwargs)
        endtime = datetime.datetime.now()
        print(
            '{}, runtime: {}'.format(
                func.__name__, 
                endtime - starttime
            )
        )
        return out_func
    return with_runtime


@count_runtime
def power2(x):
    time.sleep(2)
    return x**2


def main():
    y = power2(5)
    print(y)


if __name__ == "__main__":
    main()
