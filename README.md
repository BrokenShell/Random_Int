## Cython Project
Let's build a Python c-extension!

### CPP Header
- `Random_Int.hpp`

### Python Extension
- `Random_Int.pyx`
- `setup.py`
- `pyproject.toml`

Please note: this repo is part of an introductory guide to creating c-extensions. As such, the code represents the simplest possible implementation to accomplish the primary goal and keep it relatively short. This is in no way an exhaustive guide, but it is complete-enough to show the performance gain of Python c-extensions where the core workload is processed at the byte code level. 

While it is possible to be ever-so-slightly more simple - by just wrapping Python with Cython, and skipping the C++ layer. The performance benefit over vanilla Python is just not worth it. You still take on a large amount of complexity, but it's not as fast as using C++ at the core. 

For best results, it's recommended to use the most recent version of Python.
