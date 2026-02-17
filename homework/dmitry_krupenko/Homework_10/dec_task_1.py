

def finish_me(func):
    def wrapper(*args):
        result4 = func(*args)
        print('finished')
        return result4
    return wrapper


@finish_me
def example(text):
    print(text)


example('any value')
