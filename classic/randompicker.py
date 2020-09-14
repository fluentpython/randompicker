"""
A random picker is a collection with a ``pick`` method that pops one
random item each time it's called.

    >>> n = 100
    >>> tokens = set(range(1, n+1))
    >>> hat = RandomPicker(tokens)
    >>> picked = []
    >>> for _ in range(n):
    ...    token = hat.pick()
    ...    assert token in tokens
    ...    picked.append(token)
    ...
    >>> set(picked) == tokens
    True
    >>> picked != sorted(picked)
    True

When exhausted, ``pick`` raises ``LookupError``:

    >>> hat.pick()
    Traceback (most recent call last):
      ...
    LookupError: no more items

"""

import random

class RandomPicker():
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError as e:
            raise LookupError('no more items') from e
