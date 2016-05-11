#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 11/5/2016 5:22 PM

Author: Qu Dong

Python implementation of http://algs4.cs.princeton.edu/14analysis/TwoSum.java.html


"""
import urllib

_1Kints = 'http://algs4.cs.princeton.edu/14analysis/1Kints.txt'
_2Kints = 'http://algs4.cs.princeton.edu/14analysis/2Kints.txt'
_4Kints = 'http://algs4.cs.princeton.edu/14analysis/4Kints.txt'
_8Kints = 'http://algs4.cs.princeton.edu/14analysis/8Kints.txt'
_16Kints = 'http://algs4.cs.princeton.edu/14analysis/16Kints.txt'
_32Kints = 'http://algs4.cs.princeton.edu/14analysis/32Kints.txt'
_1Mints = 'http://algs4.cs.princeton.edu/14analysis/1Mints.txt'

def load_dfile(url):
    data = urllib.request.urlopen(url)
    data = data.readlines()
    return [int(x.decode()) for x in data]

d1 = load_dfile(_1Kints)
print(d1)
print(len(d1))

if __name__ == "__main__":
    pass

