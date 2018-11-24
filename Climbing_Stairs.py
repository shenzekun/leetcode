"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶



思路：
使用递推，比如三阶，那么就是 f(n) = f(n-1) + f(n),其中，f(n) 代表有多少种，也就是求 f(3)
只有1个阶梯的时候就f(1) = 1,两个阶梯的时候就是 f(2) = 2,所以3个阶梯f(3) = 3
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        one_step = 1
        two_step = 2
        all_step = 0
        for _ in range(2,n):
            all_step = one_step + two_step
            one_step,two_step = two_step,all_step
            
        return all_step
        