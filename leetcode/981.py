# -*- coding: utf8 -*-


"""
创建一个基于时间的键值存储类 TimeMap，它支持下面两个操作：

1. set(string key, string value, int timestamp)

存储键 key、值 value，以及给定的时间戳 timestamp。
2. get(string key, int timestamp)

返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp。
如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
如果没有值，则返回空字符串（""）。
 

示例 1：

输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
输出：[null,null,"bar","bar",null,"bar2","bar2"]
解释： 
TimeMap kv;  
kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1  
kv.get("foo", 1);  // 输出 "bar"  
kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"）  
kv.set("foo", "bar2", 4);  
kv.get("foo", 4); // 输出 "bar2"  
kv.get("foo", 5); // 输出 "bar2"  

示例 2：

输入：inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
输出：[null,null,null,"","high","high","low","low"]
 

提示：

所有的键/值字符串都是小写的。
所有的键/值字符串长度都在 [1, 100] 范围内。
所有 TimeMap.set 操作中的时间戳 timestamps 都是严格递增的。
1 <= timestamp <= 10^7
TimeMap.set 和 TimeMap.get 函数在每个测试用例中将（组合）调用总计 120000 次。
"""


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.key_tamps_map = {}

    def find(self, arr, target):
        """
        从有序数组查找target
        使用二分查找
        :param arr:
        :param target:
        :return:
        """
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        key_tamp = "{key}_{timestamp}".format(key=key, timestamp=timestamp)
        self.data[key_tamp] = value
        if self.key_tamps_map.get(key) is not None:
            if timestamp not in self.key_tamps_map[key]:
                self.key_tamps_map[key].append(timestamp)
        else:
            self.key_tamps_map[key] = [timestamp]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        key_tamp = "{key}_{timestamp}".format(key=key, timestamp=timestamp)
        # 字典中找不到key
        if self.data.get(key_tamp) is None:
            # 从key_tamps_map查找 比timestamp小的值
            timestamps = self.key_tamps_map[key][::]
            timestamps.append(timestamp)
            timestamps.sort()
            idx = self.find(timestamps, timestamp)
            if idx == -1 or idx == 0:
                return ""
            else:
                timestamp = timestamps[idx - 1]
                key_tamp = "{key}_{timestamp}".format(key=key, timestamp=timestamp)
                return self.data.get(key_tamp, "")
        else:
            return self.data.get(key_tamp, "")


class TimeMap2(object):

    def __init__(self):
        """
        超时
        Initialize your data structure here.
        """
        self.data = {}

    def find(self, arr, target):
        """
        从有序数组查找小于等于target
        使用二分查找
        :param arr:
        :param target:
        :return:
        """
        low = 0
        high = len(arr) - 1
        res = ""
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid][1] <= target:
                low = mid + 1
                res = arr[mid][0]
            else:
                high = mid - 1
        return res

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.data:
            return ""
        return self.find(self.data[key], timestamp)


if __name__ == '__main__':
    tm = TimeMap2()
    # arr = [10, 20]
    # print(tm.find(arr, 15))
    tm.set("love", "high", 10)
    tm.set("love", "low", 20)
    print(5, tm.get("love", 5))
    print(10, tm.get("love", 10))
    print(15, tm.get("love", 15))
    print(20, tm.get("love", 20))
    print(25, tm.get("love", 25))
    # print(tm.get("foo", 3))
    # tm.set("foo", "bar2", 4)
    # print(tm.get("foo", 0))
