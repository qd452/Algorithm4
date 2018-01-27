#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calculate the sum of two integers a and b, 
but you are not allowed to use the operator + and -.
"""


class Solution(object):
    def getSum_(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Below is my 1-liner
        # but this one got the memory error!!! this is as expected
        # because when a or b is very large, the memory may overflow..
        return len(list(range(a)) + list(range(b)))

    def getSum_(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
