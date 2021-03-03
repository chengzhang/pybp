# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例 1：
# 输入：l1 = [1, 2, 4], l2 = [1, 3, 4]
# 输出：[1, 1, 2, 3, 4, 4]
#
# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]
#
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        sentinel = head
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val > p2.val:
                p1, p2 = p2, p1
            sentinel.next = p1
            sentinel = p1
            p1 = p1.next
        if not p1 and p2:
            sentinel.next = p2
        if not p2 and p1:
            sentinel.next = p1
        return head.next
