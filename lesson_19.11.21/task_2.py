def type_logger(funk_decorate):
    def wrapper_args(*args):
        res = funk_decorate(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for i in args:
                print(f'{i}: {type(i)}')
        return res

    return wrapper_args


@type_logger
def volume_cube(edge, *args):
    return edge ** 3


s = volume_cube(2, 3, 5)
