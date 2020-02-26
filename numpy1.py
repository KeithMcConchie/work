import numpy as np
def rswap(a, r1, r2):
    a[[r1-1, r2-1]] = a[[r2-1, r1-1]]
def rmult(a, s, r):
    a[r-1] *= s    
def rmultadd(a, s, r1, r2):
    a[r2-1] += s*a[r1-1]

my_array = np.arange(12).reshape(3, 4)
print(my_array)
my_array[:,[0, 1]] = my_array[:,[1, 0]]
print(my_array)

# a = np.arange(15).reshape(3, 5)
# a = np.array([[1, 1, 1, 2], [2, 3, 1, 3], [1, -1, -2, -6]], dtype=np.float64)
# print(a)
# print(type(a))
# print(a[1, 2])
# a = np.array([[1, 1, 1], [2, 3, 1], [1, -1, -2]])
# b = np.array([[2], [3], [-6]])
# a = np.concatenate((b, a))
# print(a)
# print(b)
# rmultadd(a, -2, 1, 2)
# rmultadd(a, -1, 1, 3)
# print(a)
# rmultadd(a, -1, 2, 1)
# rmultadd(a, 2, 2, 3)
# print(a)
# rmult(a, -(1/5), 3)
# print(a)
# rmultadd(a, -2, 3, 1)
# rmultadd(a, 1, 3, 2)
# print(a)
# a = np.array([[1, 1, 1], [2, 3, 1], [1, -1, -2]])
# b = np.array([2, 3, -6])
# x = np.linalg.solve(a, b)
# print(x)
# a = np.array([[1, -2, 4], [2, -1, 5], [-1, 3, -3]])
# b = np.array([12, 18, -8])
# x = np.linalg.solve(a, b)
