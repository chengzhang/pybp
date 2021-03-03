from typing import List
import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if self.val == other.val:
            return self.next == other.next
        else:
            return False

    @classmethod
    def from_list(cls, numbers: List[int]):
        if not numbers:
            return None
        return ListNode(val=numbers[0], next=ListNode.from_list(numbers[1:]))

    def __repr__(self):
        p = self
        values = []
        while p:
            values.append(p.val)
            p = p.next
        return str(values)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        p1 = l1
        p2 = l2
        pr = result
        overflow = 0
        while True:
            if not p1 and not p2 and not overflow:
                break
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            sum = v1 + v2 + overflow
            val = sum % 10
            overflow = sum // 10
            pr.next = ListNode(val)
            pr = pr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return result.next


if __name__ == '__main__':
    test_cases = [
        (ListNode.from_list([2, 4, 3]), ListNode.from_list([5, 6, 4]), ListNode.from_list([7, 0, 8]))
    ]
    s = Solution()
    for case in test_cases:
        l1, l2, golden = case
        result = s.addTwoNumbers(l1, l2)
        assert result == golden
