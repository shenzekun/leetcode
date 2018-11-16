""" 
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

https://ws2.sinaimg.cn/large/006tNbRwly1fx9x9ijscij307607o0su.jpg

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。


思路：
使用 dfs 遍历每一行，在每一行的同时遍历每一列，同时我们知道，竖和撇捺都是攻击范围，因此跳过
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        self.res = []
        self.cols, self.pie, self.na = set(), set(), set()
        self.dfs(n, 0, [])
        return [["."*j + "Q" + "." * (n-j-1) for j in i] for i in self.res]

    def dfs(self, n, row, state):
        if row >= n:
            self.res.append(state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row-col in self.na:  # 如果在攻击范围内的话，就跳过
                continue

            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row-col)

            self.dfs(n, row+1, state + [col])

            # 返回状态
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row-col)
