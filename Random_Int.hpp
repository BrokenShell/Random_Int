#pragma once
#include <random>

namespace RandomInt {
    using Integer = long long;

    namespace Engine {
        using Twister = std::mt19937_64;
        using Shuffle = std::shuffle_order_engine<Twister, 64>;
        using Discard = std::discard_block_engine<Shuffle, 24, 16>;
        Discard Hurricane {std::random_device()()};
    }

    auto random_int(Integer lo, Integer hi) -> Integer {
        std::uniform_int_distribution<Integer> distribution {lo, hi};
        return distribution(Engine::Hurricane);
    }
}
