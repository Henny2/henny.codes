# decorators are used a lot in python
# simple example to demonstrate the way to use it
# creating a logger decorator
import time


def logger(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f'The function took {t2-t1} seconds.')
    return wrapper


@logger
def test_function():
    summ = 0
    for i in range(0, 1000):
        summ += i
    print(summ)


test_function()


# why this works?
# functions in python are objects
# what it does?
# it aliases the function like this:
# test_function = logger(test_function)
# and a nicer way to write that is by using the decorators @logger
# with the decorator it basically replaces the "test_function()"
# call with "test_function = logger(test_function)" at runtime
