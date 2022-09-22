#distutils: language = c++

cdef extern from "Random_Int.hpp":
    int _random_int "random_int"(int, int)


def random_int(lo: int, hi: int) -> int:
    return _random_int(lo, hi)
