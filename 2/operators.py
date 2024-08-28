from functools import partial
import logging

class Infix(object):
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q):
    raise NotImplementedError

@Infix
def iff(p, q):
    raise NotImplementedError

@Infix
def xor(p, q):
    raise NotImplementedError

@Infix
def eq(p, q):
    raise NotImplementedError


