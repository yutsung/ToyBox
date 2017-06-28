"""
"""
from functools import wraps
import time

def count_runtime(func):
    @wraps(func)
    def with_runtime():
        starttime = time.time()
        func()
        endtime = time.time()
        print("runtime: %10.8f" % (endtime-starttime))
        return func()
    return with_runtime


@count_runtime
def hello_world():
    return "Hello World"


def main():
    string = hello_world()
    print(string)


if __name__=="__main__":
    main()
