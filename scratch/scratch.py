def rect_iter(start=1, asymmetric=True):
    """
    Return a generator which iterates over pairs of integers (i, j) in a regular pattern.

    If :param asymmetric:=True, i < j for all pairs.
    """
    i = j = start
    if asymmetric:
        while True:
            j += 1
            while i < j:
                yield i, j
                i += 1
            j += 1
            while i > 1:
                yield i, j
                i -= 1

