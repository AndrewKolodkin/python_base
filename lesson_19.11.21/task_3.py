from  functools import wraps


def val_checker(callback):
    def checkets_func(func):
        @wraps(func)
        def wrapper_args(*args):
            for arg in args:
                if not callback(arg):
                    print (f'error ! {arg}')
            return func(*args)

        return wrapper_args

    return checkets_func


@val_checker(lambda edge: edge > 0)
def volume_cube(edge, *args):
    return edge ** 3

s = volume_cube(7)
print(s)
s = volume_cube(-5)
print(s)