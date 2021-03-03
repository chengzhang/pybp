class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        segs = s.split(' ')
        if len(segs) != len(pattern):
            return False
        seg_2_pat = {}
        pat_2_seg = {}
        for s, p in zip(segs, pattern):
            if s in seg_2_pat:
                if seg_2_pat[s] != p:
                    return False
                else:
                    continue
            if p in pat_2_seg:
                return False
            seg_2_pat[s] = p
            pat_2_seg[p] = s
        return True


if __name__ == '__main__':
    test_cases = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
    ]
    s = Solution()
    for case in test_cases:
        pat, segs, golden = case
        result = s.wordPattern(pat, segs)
        assert result == golden
