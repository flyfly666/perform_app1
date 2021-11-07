# import cProfile
# import re
#
# cProfile.run('re.compile("foo|bar")')

import profile


# def original():
#     global fib, fib_seq
#
#     def fib(n):
#         if n <= 1:
#             return n
#         else:
#             return fib(n - 1) + fib(n - 2)
#
#     def fib_seq(n):
#         seq = []
#         if n > 0:
#             seq.extend(fib_seq(n - 1))
#         seq.append(fib(n))
#         return seq
#
#     profile.run('print(fib_seq(20))')
#

# original()


class cached:
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = self.fn(*args)
            return self.cache[args]


@cached
def fib(n):
    a, b = 0, 1
    # if n <= 1:
    #     return n
    # else:
    #     return fib(n - 1) + fib(n - 2)
    for i in range(0, n):
        a, b = b, a+b
    return a


@cached
def fib_seq(n):
    seq = []
    # if n > 0:
    #     seq.extend(fib_seq(n - 1))
    # seq.append(fib(n))
    for i in range(0, n+1):
        seq.append(fib(i))
    return seq

# @cached
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# def fib_seq(n):
#     seq = []
#     if n > 0:
#         seq.extend(fib_seq(n - 1))
#     seq.append(fib(n))
#     return seq
#
#
# profile.run('print(fib_seq(20)) ') # 147 function calls (89 primitive calls) in 0.000 seconds

import cProfile
import pstats

# filenames = []
# profiler = cProfile.Profile()
# profiler.enable()
# for i in range(5):
#     fib_seq(1000)
# profiler.create_stats()
# stats = pstats.Stats(profiler)
# stats.strip_dirs().sort_stats('cumulative').print_stats()
# stats.print_callers()
state = {"a1": []}
a = "1,2,3"
c = a.split(",")
print(c)
print(type(c))
state['a1'].append(c)
state['a1'].append(c)
state['a1'].append(c)
print(state)

