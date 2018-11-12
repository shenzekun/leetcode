""" 
题目：给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2


思路：
定义一个 map 计算每个数的次数，找到最大的数返回这个最大的数。。。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        max = 0
        index = 0
        for i in nums:
            map[i] = map.get(i, 0) + 1
            if map[i] > max:
                max = map[i]
                index = i
        return index
