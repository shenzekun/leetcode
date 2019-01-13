""" 
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


解题思路：使用动态规划，我们从最后比较比如到6的时候，就是4+1+6，到3的时候就是3+min(f(6),f(5))...
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        
        res = triangle[-1]
        
        for i in range(len(triangle) - 2,-1,-1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j],res[j+1]) + triangle[i][j]
        return res[0]