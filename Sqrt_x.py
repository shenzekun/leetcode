"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。


思路：
由于 x^2是单调递增，因此使用二分法
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l, r = 1, x
        while l <= r:
            m = int((l+r)/2)
            if m == x/m:
                return m
            elif m > x/m:
                r = m-1
            else:
                l = m+1
                res = m
        return res
