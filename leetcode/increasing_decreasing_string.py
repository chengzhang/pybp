class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_index = lambda x: ord(x) - ord('a')
        index_char = lambda x: chr(ord('a') + x)
        cnt_arr = [0] * 26
        for i in s:
            cnt_arr[char_index(i)] += 1
        N = len(s)
        result = ''
        while N > 0:
            for i in range(26):
                if cnt_arr[i] > 0:
                    result += index_char(i)
                    cnt_arr[i] -= 1
                    N -= 1
            for i in range(26):
                if cnt_arr[25-i] > 0:
                    result += index_char(25-i)
                    cnt_arr[25-i] -= 1
                    N -= 1
        return result

if __name__ == '__main__':
    test_cases = [
        ('aaaabbbbcccc', 'abccbaabccba'),
        ('rat', 'art'),
        ('leetcode', 'cdelotee'),
        ('ggggggg', 'ggggggg'),
        ('spo', 'ops'),
    ]
    s = Solution()
    for input, output in test_cases:
        assert s.sortString(input) == output
