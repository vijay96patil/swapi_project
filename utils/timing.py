import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()                    ### time is the function under module time
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"total time to execute - {end}")
        return result
    return wrapper
# localtime= time.asctime(time.localtime(time.time()))
# localtime
