""" 
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

思路：
使用DFS，先在 board 中搜索 word 中第一个字符，再以此字符为起点进行 DFS 搜索，若搜索出的路径与 word 一致，则在网格中存在此单词。
"""

END_OF_WORD = '#'
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return []
        if not word:
            return []
        self.result = False
        root = {}
        node = root
        for char in word:
            node = node.setdefault(char, {})
        node[END_OF_WORD] = END_OF_WORD

        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)

        return self.result

    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.result = True
            return 

        temp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i+dx[k], j+dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] in cur_dict and board[x][y] != '@':
                if self.result: # 找到就直接返回
                    return
                self.dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = temp #回溯
