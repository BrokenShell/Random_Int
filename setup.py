from distutils.core import setup, Extension
from Cython.Build import cythonize


setup(
    name="Random_Int",
    ext_modules=cythonize(
        Extension(
            name="Random_Int",
            sources=["Random_Int.pyx"],
            language="c++",
            extra_compile_args=["-std=c++20"],
        ),
    ),
    version="0.0.2",
)
