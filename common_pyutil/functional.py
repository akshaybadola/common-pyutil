from typing import Union, List, Optional, Any, Callable, Iterable, Dict
from functools import partial, reduce


def rpartial(func, *args):
    def temp(*rest):
        return func(*rest, *args)
    return temp


def maybe_is(kinds: List[type], x: Any):
    return map(partial(apply, isinstance), [(x, k) for k in kinds])


def maybe_(kinds: List[type], x: Any):
    return last_item(first_by(zip(maybe_is(kinds, x), kinds), rpartial(nth, 0)))


def maybe_then(kinds: List[type], x: Any, then: List[Callable]):
    return last_item(first_by(zip(maybe_is(kinds, x), then), rpartial(nth, 0)))(x)


def foldl(func: Callable, struct: Iterable):
    it = iter(struct)
    yield(func(next(it)))


def first_by(struct: Optional[Iterable], by: Callable, predicate: Callable = identity):
    if struct:
        it = iter(struct)
        while True:
            try:
                x = next(it)
                if predicate(by(x)):
                    return x
            except StopIteration:
                return None


def last_item(struct: Optional[Iterable]):
    if struct:
        it = iter(struct)
        while True:
            try:
                x = next(it)
            except StopIteration:
                return x


def first(struct: Iterable, predicate: Callable = identity):
    return first_by(struct, identity, predicate)


def car(struct: Iterable):
    return next(iter(struct))


def nth(struct: Iterable, indx: int):
    it = iter(struct)
    i = 0
    x = None
    while i <= indx:
        try:
            x = next(it)
            i += 1
        except StopIteration:
            break
    return x


def applify(func: Callable, struct: Iterable[Iterable]):
    return map(partial(apply, func), struct)


def apply(func: Callable, args: List):
    return func(*args)


def seq(*funcs: Callable) -> Callable:
    """Alias for thunkify
    """
    return thunkify(*funcs)


def identity(x: Any):
    """Identity function.

    Example:
        identity(10) == 10
        identity(None) == None
    """
    return x


def pipe(*args: Callable) -> Callable:
    """Perform a function composition left to right.

    Example:
        def f(x: int):
            print(x)
            return str(x)

        def g(x: str):
            return "func g " + x

        def h(x: str):
            return "func h " + x

        pipe(f, g, h)(10)   # prints 10 and returns "func h func g 10"

    """
    return partial(reduce, lambda x, y: y(x), args)


def compose(*args: Callable) -> Callable:
    """Perform a function composition right to left."""
    return partial(reduce, lambda x, y: y(x), args[::-1])


def thunkify(*args: Callable) -> Callable:
    """Creates a thunk out of a function.

    A thunk delays a calculation until its result is needed, providing lazy
    evaluation of arguments. Can be used for side effects.

    Example:
        def f(x: int):
            print("func f", x)

        def g():
            print("func g")

        val = 10
        thunk = thunkify(partial(f, val), g)
        thunk()   # prints "func f 10" and "func g"

        # Or if val won't be available till later
        thunk = thunkify(f, lambda *_: g())
        some_other_func(arg1, arg2, thunk)

        # In some_other_func
        val = 20
        thunk(val)   # prints "func f 20" and "func g"

    """
    def thunk(*_args):
        for a in args:
            a(*_args)
    return thunk


def print_lens(obj: Optional[Dict], *args, prefix="") -> Any:
    """Return a value in a nested object and also print it.

    Like :func:`lens` but with more feedback
    """
    if obj is None:
        print(prefix + " (NOT FOUND)")
        return None
    elif args:
        return print_lens(obj.get(args[0]), *args[1:],
                          prefix=(prefix + " -> " if prefix else "") + str(args[0]))
    else:
        print(prefix + " -> " + str(obj))
        return obj


def lens(obj: Optional[Dict], *args) -> Any:
    """Return a value in a nested object.
    """
    if obj is None:
        return None
    elif args:
        return lens(obj.get(args[0]), *args[1:])
    else:
        return obj


def difference(a: Iterable, b: Iterable) -> set:
    """Return set difference of two iterables"""
    a = set([*a])
    b = set([*b])
    return a - b


def intersection(a: Iterable, b: Iterable) -> set:
    """Return intersection of two iterables"""
    a = set([*a])
    b = set([*b])
    return a.intersection(b)


def union(a: Iterable, b: Iterable) -> set:
    """Return union of two iterables"""
    a = set([*a])
    b = set([*b])
    return a.union(b)


def concat(list_var: Iterable[List]) -> List:
    """Concat all items in a given list of lists"""
    temp = []
    for x in list_var:
        temp.extend(x)
    return temp


def takewhile(predicate, seq):
    """Lazily evaluated takewhile

    :param predicate: First failure of predicate stops the iteration. Should return bool
    :param seq: Sequence from which to take
    :returns: filtered sequence
    :rtype: Same as `seq`

    """
    it = iter(seq)
    _next = it.__next__()
    while predicate(_next):
        try:
            yield _next
            _next = it.__next__()
        except StopIteration:
            return None