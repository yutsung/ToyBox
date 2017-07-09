"""
"""
from functools import wraps
import time

def count_runtime(func):
    @wraps(func)
    def with_runtime(*args, **kwargs):
        starttime = time.time()
        out_func = func(*args, **kwargs)
        endtime = time.time()
        print("runtime: %10.8f" % (endtime-starttime))
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