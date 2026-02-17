from functools import wraps


def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)

        result = None
        for _ in range(count):
            result = func(*args, **kwargs)

        return result

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=8)


# доп задание

def repeat_me(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
