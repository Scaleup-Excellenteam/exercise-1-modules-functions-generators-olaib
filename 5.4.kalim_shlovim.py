SPACE = ' '


def interleaveGenerator(*args):
    """ accepts one or more iterable parameters, and returns a list of the interwoven members.
    :param args: one or more iterable parameters
    :return: list of the interwoven elements
    """
    args = get_list_of_lists(args)
    for i in range(len(args[0])):
        yield from [arg[i] for arg in args]


def get_list_of_lists(args):
    """ check if all in same size and convert to lists
    :param args:
    :return: list of lists of the arguments
    """
    # //check if all in same size
    size = len(args[0])
    assert all(len(arg) == size for arg in args), "All arguments must be the same size"
    args = [list(arg) for arg in args]
    return args


def interleave(*args):
    """ without generators method
    accepts one or more iterable parameters, and returns a list of the interwoven members.
    :param args: one or more iterable parameters
    :return: list of the interwoven elements
    :see: interleaveGenerator for generator method
    """
    args = get_list_of_lists(args)
    return [arg[i] for arg in args for i in range(len(args[0]))]


# ================== MAIN ==================
if __name__ == '__main__':
    leaves_list = ('abc', [1, 2, 3], ('!', '@', '#'))
for leave in interleaveGenerator(*leaves_list):
    print(leave, end=SPACE)
print("\n============ generator ============")
for leave in interleave(*leaves_list):
    print(leave, end=SPACE)
