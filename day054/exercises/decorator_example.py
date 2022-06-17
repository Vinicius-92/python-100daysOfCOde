import time


def delay_decorator(function):
    def wrapper_function():
        # This way you can do something before the function
        time.sleep(2)
        function()
        # This way you can do something with the function (ex. exec twice)
        function()
        # This way you can do something after the function
    return wrapper_function()


@delay_decorator
def say_hello():
    print("hello")
