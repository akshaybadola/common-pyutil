from functools import partial, reduce


def takewhile(predicate, seq):
    """Lazily evaluated takewhile

    :param predicate: First failure of predicate stops the iteration. Should return bool
    :param seq: Sequence from which to take
    :returns: filtered sequence
    :rtype: Same as `seq`

    """
    if iter(seq):
        it = iter(seq)
    else:
        return None
    _next = it.__next__()
    while predicate(_next):
        try:
            yield _next
            _next = it.__next__()
        except StopIteration:
            return None
