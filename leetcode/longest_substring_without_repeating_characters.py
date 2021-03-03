import pdb

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        start = 0
        last_pos = {}
        for i, chr in enumerate(s):
            #pdb.set_trace()
            if chr not in last_pos:
                last_pos[chr] = i
            elif last_pos[chr] >= start:
                start = last_pos[chr] + 1
            last_pos[chr] = i
            result = max(i - start + 1, result)
        return result


if __name__ == '__main__':
    test_cases = [
        ("aabaab!bb", 3),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]

    s = Solution()
    for case  in test_cases:
        st, golden = case
        result = s.lengthOfLongestSubstring(st)
        assert result == golden
