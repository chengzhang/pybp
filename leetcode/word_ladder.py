# coding = utf8
"""base"""

import pdb

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        begin_set = set([beginWord])
        end_set = set([endWord])
        dist = self.bfs(word_set, begin_set, end_set, 2)
        return dist

    def bfs(self, word_set, begin_set, end_set, dist):
        if len(begin_set) > len(end_set):
            return self.bfs(word_set, end_set, begin_set, dist)
        if not len(begin_set):
            return 0
        new_begin_set = set()
        for begin_word in begin_set:
            candidates = self.next_candidates(begin_word)
            for candidate in candidates:
                if candidate in end_set:
                    return dist
                if candidate in word_set:
                    new_begin_set.add(candidate)
        for word in new_begin_set:
            word_set.remove(word)
        return self.bfs(word_set, new_begin_set, end_set, dist+1)

    def next_candidates(sef, word):
        candidates = []
        chars = list(word)
        for i in range(len(chars)):
            old_char = chars[i]
            for c in range(26):
                new_char = chr(ord('a') + c)
                if old_char != new_char:
                    chars[i] = new_char
                    candidates.append(''.join(chars))
            chars[i] = old_char
        return candidates


    def is_adjacent(self, a, b):
        n_diff = 0
        for i, j in zip(a, b):
            if i != j:
                n_diff += 1
                if n_diff > 1:
                    return 0
        if n_diff == 1:
            return 1
        return 0

if __name__ == '__main__':
    solution = Solution()
    result = solution.ladderLength("hit", "cog", ["hot", "cog", "dot", "dog", "hit", "lot", "log"])
    print(result)
