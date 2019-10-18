# -*- coding: utf8 -*-



def mid_search(arr,target):
    low,height = 0,len(arr)
    while 1:
        mid = (low + height) // 2
        if arr[mid] == target:
            print(mid,target)
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            height = height -1

def twoSum(nums, target):
    """
    求列表中两数之和，并返回两数的索引
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    else:
        return []

def twoSum2(nums, target):
    """
    求列表中两数之和，并返回两数的索引
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_map = {}
    for i,v in enumerate(nums):
        t = target - v
        if t in nums:
            return [num_map[t],i]
        num_map[v] = i
    return []



def binary_search(arr, target):
    """
    二分查找
    :param arr:
    :param target:
    :return:
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    i,j = 0,1
    pivot_index = 0
    length = len(nums)
    while i < length and j < length:
        if nums[i] > nums[j]:
            pivot_index = i
            break
        i += 1
        j += 1
    left_arr = nums[:pivot_index + 1]
    right_arr = nums[pivot_index + 1:]
    left_mid = binary_search(left_arr, target)
    right_mid = binary_search(right_arr, target)
    if left_mid is not None and right_mid is None:
        return left_mid
    elif right_mid is not None and left_mid is None:
        return right_mid + len(left_arr)
    else:
        return -1


if __name__ == '__main__':
    # arr = [1,5,8,10,13,16,18,20]
    # # mid_search(arr, 16)
    # nums = [3,2,4]
    # target = 6
    # res = twoSum2(nums, target)
    # print (res)
    nums = [4,5,6,7,0,1,2]
    print(search(nums, 0))
