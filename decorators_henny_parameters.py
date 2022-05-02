# decorators with parameters
import time


def logger(func):
    # putting args and kwargs, to account for arguments
    # passed to the function
    # we don't know if and what arguments the
    # wrapped function will have,
    # args and kwargs account for that
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f'The function took {t2-t1} seconds.')
        # print the arguments of the function
        print(
            f"""Function ran with the following arguments:
             {[a for a in args]}""")
    return wrapper


@logger
# assuming num is >=0
def test_function(num):
    summ = 0
    for i in range(0, num):
        summ += i
    print(summ)


test_function(10)
