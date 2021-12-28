# -*- coding: utf-8 -*-

# @File    : lru_algorithm.py
# @Date    : 2021-12-17
# @Author  : windyzhao
import collections

"""
使用有序字典存储
"""


class LRUAlgorithm(object):
    def __init__(self, length):
        self.order_dict = collections.OrderedDict()
        self.length = length  # 最长的限制
        self.now_length = 0  # 当前长度

    def get(self, key):
        value = self.order_dict.pop(key, None)
        if value is None:
            return -1

        self.order_dict[key] = value  # 放到头部

        return value

    def put(self, key, values):
        if self.now_length >= self.length:
            self.order_dict.popitem(last=False)  # 去掉最后一个（最先那个）

        value = self.order_dict.pop(key, False)

        self.order_dict[key] = value or values

        self.now_length += 1


if __name__ == '__main__':
    lru = LRUAlgorithm(length=3)
    print("a:{}".format(lru.get("a")))
    print("=============")
    lru.put("a", 1)
    lru.put("b", 2)
    lru.put("c", 3)
    lru.put("d", 4)
    lru.put("e", 5)
    print("=============")
    print("a:{}".format(lru.get("a")))
    print("b:{}".format(lru.get("b")))
    print("c:{}".format(lru.get("c")))
    print("d:{}".format(lru.get("d")))
    print("e:{}".format(lru.get("e")))
    print("c:{}".format(lru.get("c")))
    print("============")
    print(lru.order_dict)
