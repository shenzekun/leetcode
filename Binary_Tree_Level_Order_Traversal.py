import collections
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]


思路：
① 使用 dfs 遍历，每次记录下 level 层数。时间复杂度为O(n)
② 使用 bfs 遍历
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 方法一
class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, node, level):
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        if node.left:  # 如果有左子树
            self.dfs(node.left, level + 1)
        if node.right:  # 如果有右子树
            self.dfs(node.right, level + 1)


# 方法二


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level_size = len(queue)  # 获取当前层
            current_level = []
            for _ in range(level_size):  # 遍历，将当前的层的元素加到current_level里面
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
