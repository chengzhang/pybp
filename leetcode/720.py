# 720.词典中最长的单词
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
# 若无答案，则返回空字符串。
#
# 示例 1：
# 输入：
# words = ["w", "wo", "wor", "worl", "world"]
# 输出："world"
# 解释： 单词 "world" 可由 "w", "wo", "wor", 和 "worl" 添加一个字母组成。
#
# 示例 2：
# 输入：
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出："apple"
# 解释： "apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply"。
#
# 提示：
# 所有输入的字符串都只包含小写字母。
# words数组长度范围为[1, 1000]。
# words[i] 的长度范围为[1, 30]。
#
# 通过次数13, 923 提交次数29, 002

class TrieNode(object):
    def __init__(self, char=None, word=None):
        self.char = char
        self.word = word
        self.son = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode(word='')

    def add(self, s):
        node = self.root
        for i, char in enumerate(s):
            if char not in node.son:
                son_node = TrieNode(char)
                node.son[char] = son_node
            else:
                son_node = node.son[char]
            node = son_node
        node.word = s


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for i, word in enumerate(words):
            trie.add(word)
        def __dfs(node, depth):
            res, res_len = node.word, depth
            for char, son_node in node.son.items():
                if not son_node.word:
                    continue
                sub, sub_len = __dfs(son_node, depth+1)
                if res_len < sub_len:
                    res, res_len = sub, sub_len
                elif res_len == sub_len and res > sub:
                    res = sub
            return res, res_len
        result, result_len = __dfs(trie.root, 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (["w", "wo", "wor", "worl", "world"], 'world'),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], 'apple'),
    ]
    for case in test_cases:
        words, golden = case
        result = solution.longestWord(words)
        print(result, golden)
        assert result == golden
