import pdb

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N = len(nums1) + len(nums2)
        left, right = self.mid_index(N)
        pdb.set_trace()
        mid1 = self.get_value_of_order(nums1, nums2, left)
        if left != right:
            mid2 = self.get_value_of_order(nums1, nums2, right)
        else:
            mid2 = mid1
        return (mid1 + mid2) / 2

    def mid_index(self, n):
        if n % 2 == 1:
            left = right = n // 2
        else:
            left = n // 2 - 1
            right = n // 2
        return left, right

    def get_value_of_order(self, nums1, nums2, order):
        left_bound_1, left_bound_2 = 0, 0
        right_bound_1 = min(len(nums1), order+1)
        right_bound_2 = min(len(nums2), order+1)
        def __order_of_value(value, nums, lb, rb):
            while lb < rb:
                mid = (lb + rb) // 2
                if nums[mid] <= value:
                    lb = mid + 1
                else:
                    rb = mid
            return lb

        def __value_of_order(lb1, rb1, lb2, rb2, order):
            if lb1 >= rb1:  # n1 empty
                return nums2[lb2 + order]
            elif lb2 >= rb2:  # n2 empty
                return nums1[lb1 + order]
            mid1 = (lb1 + rb1) // 2  # order 1: mid1 - lb1
            mid2 = __order_of_value(nums1[mid1], nums2, lb2, rb2)  # order 2: mid2 - lb2
            mid_order = mid1 - lb1 + mid2 - lb2
            if mid_order == order:
                return nums1[mid1]
            elif mid_order < order:
                return __value_of_order(mid1 + 1, rb1, mid2, rb2, order - mid_order - 1)
            else:
                return __value_of_order(lb1, mid1, lb2, mid2, order)

        return __value_of_order(left_bound_1, right_bound_1, left_bound_2, right_bound_2, order)


if __name__ == '__main__':
    test_cases = [
        ([1,2], [3,4], 2.5),
        ([1,3], [2], 2.0),
        ([0,0], [0,0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]
    s = Solution()
    for case in test_cases:
        nums1, nums2, golden = case
        result = s.findMedianSortedArrays(nums1, nums2)
        pdb.set_trace()
        assert result == golden
