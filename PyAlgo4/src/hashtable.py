#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In general, rehash(pos)=(pos+skip)%sizeoftable.
It is important to note that the size of the “skip” must be such that all the slots in the table
will eventually be visited. Otherwise, part of the table will be unused.

To ensure this, it is often suggested that the table size be a prime number.
"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"


def gethashvalue(key_v, tablesize):
    """
    key_str must be immutable, just like the key values in dict.
    if the key_str is mutable, the hash value will also be changed

    :param key_v: integer, string, tuple of integer or string
    :param tablesize:
    :return:
    """
    if isinstance(key_v, str):
        return sum(ord(i) for i in key_v) % tablesize
    elif isinstance(key_v, int):
        return key_v % tablesize
    elif isinstance(key_v, tuple):
        return sum(ord(j) for i in key_v for j in str(i)) % tablesize


class HastTable():
    def __init__(self, tablesize=11):
        self.key = [None] * tablesize
        self.value = [None] * tablesize
        self.size = 0
        self.tablesize = tablesize

    def put(self, k, v):
        """

        :param k:
        :param v:
        :return:
        """
        hv = gethashvalue(k, self.tablesize)
        if self.key[hv] == None:  # 如果那个slot还是空的
            self.key[hv] = k
            self.value[hv] = v
        else:
            # now we already know hashvalue is already in the keys, we need to check if the key value are the same
            if self.key[hv] == k:  # if k is already in the self.key list, we just update the value
                self.value[hv] = v
            else:  # means different k share the same hash value, we need then re-hash (quadratic probing)
                # re-hashing techniques
                rehv = (hv + 1) % self.tablesize
                loop = 2
                while self.key[rehv] != None:
                    rehv = (rehv + loop ** 2) % self.tablesize
                    loop += 1
                self.key[rehv] = k
                self.value[rehv] = v
        self.size += 1

    def get(self, k, d=None):
        """
        get the value based on the key value
        :param k:
        :param d: default
        :return:
        """
        hv = gethashvalue(k, self.tablesize)
        if self.key[hv] == None:
            return d
        else:
            if self.key[hv] == k:
                return self.value[hv]
            else:
                rehv = (hv + 1) % self.tablesize
                loop = 2
                while self.key[rehv] != k:
                    rehv = (rehv + loop ** 2) % self.tablesize
                    loop += 1
                    if rehv == hv:
                        return d
                return self.value[rehv]

    def remove(self, k):
        hv = gethashvalue(k, self.tablesize)
        if self.key[hv] == None:
            raise KeyError(k)
        else:
            if self.key[hv] == k:
                self.key[hv] = None
                self.value[hv] = None
                self.size -= 1
            else:
                rehv = (hv + 1) % self.tablesize
                loop = 2
                while self.key[rehv] != k:
                    rehv = (rehv + loop ** 2) % self.tablesize
                    loop += 1
                    if rehv == hv:
                        raise KeyError(k)
                self.key[rehv] = None
                self.value[rehv] = None
                self.size -= 1

    def __getitem__(self, item):
        v = self.get(item)
        if not v:
            raise KeyError(item)
        return v

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __repr__(self):
        return '{' + ', '.join(
            ['{}: {}'.format(self.key[i], self.value[i]) for i in range(self.tablesize)]) + '}'

    def __str__(self):  # 感觉它更能重写repr -> 其实并不是，只是只有在console里面直接表示ht的时候，__repr__()会被调用，
        # 然而当print(), str(), format()的时候，都是__str__()被调用的
        # http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
        return '{' + ', '.join(
            ['{}: {}'.format(self.key[i], self.value[i]) for i in range(self.tablesize) if self.key[i] != None]) + '}'


if __name__ == "__main__":
    ht = HastTable(tablesize=23)
    ht.put(11, 'a')
    ht.put(22, 'b')
    ht.put(5, '5')
    ht.put(33, 'c')
    ht.put((33, 11), 'tuple3311')
    ht.put((33, 11), 'tupleeeeee3311')
    ht.put((11, 222), 'hahah')
    ht.put('a', 'abc')

    print(ht)
    print(ht.get(22))
    print(ht.get(33))
    print(ht.get(111, 'haha'))
    print(ht[22])  # enabled by __getitem__(self, key)
    try:
        print(ht[12])  # will raise KeyError
    except Exception as e:
        print(type(e), str(e))