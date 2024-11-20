def add_log(func):
    def wrapper(*args, **kwargs):
        print('%s is running' % func.__name__)
        return func(*args, **kwargs)
    return wrapper
@add_log
def add(a,b):
    return a+b
