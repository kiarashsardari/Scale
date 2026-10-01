import numpy as np
from math import sqrt
# variance = sigma(x - loc)^2/n
# scale = sqrt(variance)
def variance(nums_array):
    return ((nums_array - loc(nums_array))**2).sum()/len(nums_array)


def scale(v):
    return sqrt(v)


def loc(nums):
    return (nums).sum()/len(nums)


if __name__ == '__main__':
    arry = np.array([1,4,8,9,0])
    v = variance(arry)
    print(loc(arry))
    print(scale(v))
    print(v)