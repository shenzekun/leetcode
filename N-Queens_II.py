""" 
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

https://ws2.sinaimg.cn/large/006tNbRwly1fx9x9ijscij307607o0su.jpg

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

思路：
和上一题一样只不过输出的东西不一样
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return []
        self.res = 0
        self.cols, self.pie, self.na = set(), set(), set()
        self.dfs(n, 0, [])
        return self.res

    def dfs(self, n, row, state):
        if row >= n:
            self.res += 1
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row-col in self.na:  # 如果在攻击范围内的话，就跳过
                continue

            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row-col)

            self.dfs(n, row+1, state + [col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row-col)
