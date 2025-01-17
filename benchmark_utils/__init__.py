# `benchmark_utils` is a module in which you can define code to reuse in
# the benchmark objective, datasets, and solvers. The folder should have the
# name `benchmark_utils`, and code defined inside will be importable using
# the usual import syntax

# Import the function from the module
from .prepare_data import prepare_data

# Specify what should be imported when using wildcard import *
__all__ = ['prepare_data']