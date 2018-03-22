import math


def is_valid_nonzero(value):
    return not (isinstance(value, str) or math.isnan(value) or value == 0)
