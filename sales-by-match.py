#!/bin/python3

from collections import Counter


def sockMerchant(n, ar):
    sum = 0
    for val in Counter(ar).values():
        sum += val//2
    return sum


n = 8
arr = [10, 20, 20, 10, 30, 50, 10]
print(sockMerchant(n, arr))
