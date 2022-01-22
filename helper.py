import os
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def even(integer):
    return integer//2 == integer/2


def relative_file(file_name):
    path = os.path.split(__file__)[0]
    return os.path.join(path, file_name)
