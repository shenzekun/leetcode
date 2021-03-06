"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

思路：
还是使用 dfs
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self.dfs(root,0)
        self.result.reverse()
        return self.result
    def dfs(self, node,level):
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        if node.left:
            self.dfs(node.left,level+1)
        if node.right:
            self.dfs(node.right,level + 1)
        