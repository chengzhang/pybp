# 面试题 17.12. BiNode
# 二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，
# 也就是在原始的二叉搜索树上直接修改。
#
# 返回转换后的单向链表的头节点。
#
# 注意：本题相对原题稍作改动
#
#
#
# 示例：
#
# 输入： [4,2,5,1,3,null,6,0]
# 输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
# 提示：
#
# 节点数量不会超过 100000。
# 通过次数14,346提交次数22,879
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root, rightest = self._convert(root)
        return root

    def _convert(self, node):
        # return new tree root and rightest node
        if not node:
            return None, None
        left_head, left_rightest = self._convert(node.left)
        right_head, right_rightest = self._convert(node.right)
        node.left = None
        node.right = right_head
        if left_rightest:
            left_rightest.right = node
        root = left_head if left_head else node
        rightest = right_rightest if right_rightest else node
        return root, rightest
