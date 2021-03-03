# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
# 注意：字符串长度 和 k 不会超过 104。
#
# 示例 1：
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
#
# 示例 2：
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。

import pdb

class CharCount(object):
    def __init__(self):
        self.count = [0] * 26

    def add(self, char):
        index = ord(char) - ord('A')
        self.count[index] += 1

    def remove(self, char):
        index = ord(char) - ord('A')
        self.count[index] -= 1

    def most(self):
        return max(self.count)


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0
        begin = 0
        char_cnt = CharCount()
        for i, char in enumerate(s):
            char_cnt.add(char)
            most = char_cnt.most()
            sub_len = i - begin + 1
            if sub_len - most <= k:
                if result < sub_len:
                    result = sub_len
            else:
                char_cnt.remove(s[begin])
                begin += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ("AABABBA", 1, 4),
        ("ABAB", 2, 4),
    ]
    for case in test_cases:
        s, k, golden = case
        result = solution.characterReplacement(s, k)
        print(result, golden)
        assert result == golden
