class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        buckets = [[] for n in range(15)]
        for i in arr:
            n = self.bits(i)
            buckets[n].append(i)
        result = []
        for n in range(15):
            sub_arr = sorted(buckets[n])
            result.extend(sub_arr)
        return result

    def bits(self, x):
        n = 0
        while(x):
            if x % 2 == 1:
                n += 1
            x //= 2
        return n
