""" 
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


思路：
使用分治，x^n 如果 n 是偶数，那么可以转化成 x^(n/2) * x^(n/2), 
然后x^(n/2) 可以再转换 x^(n/4) * x^(n/4)，一直到 x^0或者 x^1,
同理，如果 n 是奇数，那么 x^n 可以看成 x * x^(n-1), 然后递归下去
时间复杂度为 O（logn）
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n/2)
