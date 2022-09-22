#pragma once
#include <random>


std::mt19937_64 Hurricane {std::random_device()()};

auto random_int(int lo, int hi) -> int {
    std::uniform_int_distribution<int> distribution {lo, hi};
    return distribution(Hurricane);
}
