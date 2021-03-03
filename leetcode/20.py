# 20. 有效的括号
# 给定一个只包括'('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 示例 # 1：
# 输入：s = "()"
# 输出：true
#
# 示例 # 2：
# 输入：s = "()[]{}"
# 输出：true
#
# 示例 # 3：
# 输入：s = "(]"
# 输出：false
#
# 示例 # 4：
# 输入：s = "([)]"
# 输出：false
#
# 示例 # 5：
# 输入：s = "{[]}"
# 输出：true
#
#提示：
# 1 <= s.length <= 104
# s 仅由括号'()[]{}' 组成
#

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        right2left = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for it in s:
            if it in '([{':
                stack.append(it)
            else:
                if not stack or stack[-1] != right2left[it]:
                    return False
                else:
                    stack.pop()
        return True


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("{[]}", True),
    ]
    for case in test_cases:
        s, golden = case
        result = solution.isValid(s)
        print(result, golden)
        assert result == golden

