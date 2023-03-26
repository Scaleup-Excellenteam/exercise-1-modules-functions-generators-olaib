def join(*chain, sep='-'):
    """
    this function joins the elements of the chain into a single list with the separator between them
    :param chain:
    :param sep:
    :return: list of chain with the separator between them
    """
    lists = [item + [sep] for item in chain]
    result = [val for sublist in lists for val in sublist]
    return result[:-1] if result else None


# ================== MAIN ==================
if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
