"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

思路：
使用 dfs 遍历，然后剪枝，左右括号都是 n 个，并且左括号必须大于右括号的数目的时候才能加右括号，时间复杂度为O(2^n)
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, '')
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:  # 如果左右括号都是 n 个
            self.list.append(result)
            return
        if left < n:
            self._gen(left+1, right, n, result + '(')
        if left > right and right < n:  # 左括号大于右括号并且此时右括号小于 n
            self._gen(left, right+1, n, result + ')')
