# 110. 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
# 示例 2：
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
# 示例 3：
# 输入：root = []
# 输出：true

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balance = self.height_and_balance(root)
        return balance

    def height_and_balance(self, root):
        if root.left:
            left_height, balance = self.height_and_balance(root.left)
            if not balance:
                return left_height, False
        else:
            left_height = 0
        if root.right:
            right_height, balance = self.height_and_balance(root.right)
            if not balance:
                return right_height, False
        else:
            right_height = 0
        if left_height > right_height + 1 or right_height > left_height + 1:
            return left_height, False
        return max(left_height, right_height) + 1, True
