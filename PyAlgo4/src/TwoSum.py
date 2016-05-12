#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 11/5/2016 5:22 PM

Author: Qu Dong

Python implementation of http://algs4.cs.princeton.edu/14analysis/TwoSum.java.html


"""
import urllib
from itertools import combinations
import time
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
from bisect import bisect_left

urldict = OrderedDict([
    ('1Kints', 'http://algs4.cs.princeton.edu/14analysis/1Kints.txt'),
    ('2Kints', 'http://algs4.cs.princeton.edu/14analysis/2Kints.txt'),
    ('4Kints', 'http://algs4.cs.princeton.edu/14analysis/4Kints.txt'),
    ('8Kints', 'http://algs4.cs.princeton.edu/14analysis/8Kints.txt'),
    ('16Kints', 'http://algs4.cs.princeton.edu/14analysis/16Kints.txt'),
    ('32Kints', 'http://algs4.cs.princeton.edu/14analysis/32Kints.txt'),
    # ('1Mints', 'http://algs4.cs.princeton.edu/14analysis/1Mints.txt'), # looks like 1M is too heavy for urllib to extract
])


def load_dfile(url):
    """
    Load the txt data file directly from the url, internet connection is needed

    :param url: the text file url
    :return: a list of integers
    """
    data = urllib.request.urlopen(url)
    data = data.readlines()
    return [int(x.decode()) for x in data]


def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end


class TwoSum():
    def __init__(self, a):
        self.a = a
        self.N = len(a)

    def print_all(self):
        for a, b in combinations(self.a, 2):
            if a + b == 0: print(a + " " + b)

    def count(self):
        cnt = 0
        for a, b in combinations(self.a, 2):
            if a + b == 0: cnt += 1
        return cnt


class TwoSumFast():
    def __init__(self, a):
        self.a = sorted(a)  # NOTE: [iterable].sort will sort the iterable, but return None
        self.N = len(a)

    def print_all(self):
        for i, d in enumerate(self.a):
            j = binary_search(self.a, -d)
            if j > i: print(i + " " + j)

    def count(self):
        cnt = 0
        for i, d in enumerate(self.a):
            j = binary_search(self.a, -d)
            if j > i: cnt += 1
        return cnt


def calculate_twosum(url, fast=False):
    """
    Load the url and calculate the two sum which is equal to 0

    :param url: the url to open
    :return: the data size in K, and the time elapsed to calculate
    """
    data = load_dfile(url)
    t_start = time.time()
    if not fast:
        obj = TwoSum(data)
    else:
        obj = TwoSumFast(data)
    cnt = obj.count()
    t_stop = time.time()
    t_delta = t_stop - t_start
    print('For N = ', obj.N, 'elapsed time = ', t_delta, 's')
    return obj.N / 1000, t_delta


if __name__ == "__main__":
    d = []
    dfast = []
    for k, v in urldict.items():
        d.append(tuple(calculate_twosum(v, fast=False)))
        dfast.append(tuple(calculate_twosum(v, fast=True)))
    df = pd.DataFrame(d, columns=['Data Size [K]', 'Normal'])
    dfast = pd.DataFrame(dfast, columns=['Data Size [K]', 'Fast'])
    fig, ax = plt.subplots(1, 1)
    df.plot(ax=ax, x='Data Size [K]', y=['Normal'])
    dfast.plot(ax=ax, x='Data Size [K]', y=['Fast'], secondary_y=True)
    ax.set_title('TwoSum Normal vs Fast')
    ax.set_xlabel('Data Size [K]')
    ax.set_ylabel('Time Elapsed [sec]')
    plt.tight_layout()
    plt.savefig('TwoSum_Normal_Fast.png')
    plt.show()
