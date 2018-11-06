"""
题目：
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


解题思路：
一遍哈希表，在进行迭代并将元素插入到map中的同时，我们还会回过头来检查map中是否已经存在当前元素所对应的目标元素。
如果它存在，那我们已经找到了对应解，并立即将其返回,时间复杂度：O(n)
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i,v in enumerate(nums):
            if (target-v) in map:
                return [map[target-v],i]
            map[v]= i
        return False
            