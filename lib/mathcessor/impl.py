from . import numbers
from math import factorial

class CrazyStaticMethodInterceptingMetaclass(type):
    def __getattr__(self, name):
        clean_name = name.replace("_", " ")

        if name.startswith("square_root_of_"):
            return int(numbers.word_to_number(clean_name[14:]) ** (1/2.0))

        if name.startswith("cube_root_of_"):
            return int(numbers.word_to_number(clean_name[12:]) ** (1/3.0))

        if name.startswith("factorial_"):
            return factorial(numbers.word_to_number(clean_name[9:]))

        if name.endswith("_squared"):
            return numbers.word_to_number(clean_name[:-8]) ** 2

        if name.endswith("_cubed"):
            return numbers.word_to_number(clean_name[:-6]) ** 3

        return numbers.word_to_number(clean_name)


class M(metaclass=CrazyStaticMethodInterceptingMetaclass):
    """Attribute access is only on instances of a class. If we want to override
    it, we need to change the class definer. Thus, this is an empty skeleton
    that only uses a custom metaclass."""
