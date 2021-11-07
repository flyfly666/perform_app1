import line_profiler
import sys

from line_profiler import LineProfiler


# @LineProfiler
# def fib(n):
#     a, b = 0, 1
#     for i in range(0, n):
#         a, b = b, a+b
#     return a
# #


def test():
    for i in range(0, 10):
        print(i ** 2)
    print("end of the function")


prof = line_profiler.LineProfiler(test)

prof.enable()
test()
prof.disable()
prof.print_stats()
