import functools as ft
import itertools as it
import operator
from collections import ChainMap, namedtuple, Counter, deque
import copy

DictRec = namedtuple("DictRec", ["key", "val"])
# for dr in map(DictRec._make, c.items()):
#     print(dr.key, dr.val)

city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
            ]

def get_state(city_state):
    return city_state[1]

a, b, c = it.groupby(city_list, get_state)
for i in a:
    print(i)

# def counter(maximum):
#     i = 0
#     while i < maximum:
#         val = (yield i)
#         if val is not None:
#             i = val
#         else:
#             i += 1
# it = counter(10)
# it.send(8)


# d = deque('ghi')
# print(list(d))
# a = DictRec(1, "hello")
# b = DictRec(2, "world")
# c = DictRec(3, "how")
# d = DictRec(4, "are")
# e = DictRec(5, "you")

# dq = deque([a, b, c, d, e], 5)
# dq2 = copy.deepcopy(dq)
# print()
# for e in dq:
#     print(id(e))
# print()
# for e in dq2:
#     print(id(e))
# dq.maxlen = 7
# dq.extend([6, 7])
# print(list(dq))

# dq.append(6)
# dq.append(7)
# print(list(dq))
# dq.appendleft(2)
# print(list(dq))
# dq2 = dq.copy()
# print(id(dq), id(dq2))
# print(list(dq), list(dq2))
