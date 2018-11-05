"""
题目：给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？



解题思路：使用两个数组，一个数组widow维护下标，另外一个res存结果，每次都维护window的大小，
如果遇到一个比 nums[window[-1]] 大的时候，就 pop 掉 window 的第一个，保证每次 window
的最左边的num[window[0]]值最大,这样就可以输出了
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window,res = [],[]
        for i,x in enumerate(nums):
            if i>=k and window[0] <= i-k: #超出 window 大小，window 存的是下标，将最前一个去掉
                window.pop(0)
            
            """
            如果新进来的元素比之前的 nums[window[-1]] 大，那就把 window 的所有下标 pop 掉，
            保证新进来这个元素的下标在 window 的最左边
            """
            while window and nums[window[-1]] <= x:  
                window.pop()
            window.append(i)
            if i >= k-1: # 如果下标大于 k - 1，就将结果输入到 res 里
                res.append(nums[window[0]])
        return res
        