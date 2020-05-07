def pair_iter(start=1, asymmetric=True, strategy='descending'):
    """
    Return a generator which iterates over pairs of integers (i, j) in a regular pattern.

    Parameters:
        :bool asymmetric: If True, i < j for all pairs. Otherwise all possible 2 tuples are traversed.
        :str strategy: Allows `ascending`, `descending`, or `alternating`. This determines if the first term is
            incremented or decremented as the second term increases. For `alternating`, they both alternate direction.
    """
    i = j = start
    if asymmetric:
        if strategy == 'alternating':
            while True:
                j += 1
                while i < j:
                    yield i, j
                    i += 1
                j += 1
                while i > 1:
                    yield i, j
                    i -= 1

        elif strategy == 'ascending':
            while True:
                j += 1
                while i < j:
                    yield i, j
                    i += 1
                i = start

        elif strategy == 'descending':
            while True:
                j += 1
                while i >= start:
                    yield i, j
                    i -= 1
                i = j

        else:
            raise ValueError("Specify a valid strategy.")

    else:
        if strategy == 'alternating':
            while True:
                yield i, j
                j += 1
                while j > start:
                    yield i, j
                    i += 1
                    j -= 1
                yield i, j
                i += 1
                while i > start:
                    yield i, j
                    i -= 1
                    j += 1

        if strategy == 'ascending':
            while True:
                yield i, j
                j += 1
                i = start
                while i < j:
                    yield i, j
                    i += 1

        if strategy == 'descending':
            while True:
                yield i, j
                j += 1
                i = j
                while i > start:
                    yield i, j
                    i -= 1

        else:
            raise ValueError("Specify a valid strategy.")
