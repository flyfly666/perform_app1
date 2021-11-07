import profile
import sys


def profiler(frame, event, arg):
    print(f"PROFILER : {event} ,{arg} ")


sys.setprofile(profiler)


def add(a, b):
    return a + b


c = add(1, 100)
print(c)
