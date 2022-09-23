#distutils: language = c++

cdef extern from "Random_Int.hpp":
    long long _random_int "RandomInt::random_int"(long long, long long)


def random_int(lo: int, hi: int) -> int:
    return _random_int(lo, hi)
