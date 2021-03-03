class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        idx_2_peers = {i: [i] for i in range(N)}
        idx_2_peer_set = {i: {i} for i in range(N)}
        chr_2_indexes = {}
        for i, chr in enumerate(s):
            if chr not in chr_2_indexes:
                chr_2_indexes[chr] = [i]
            else:
                chr_2_indexes[chr].append(i)

        max_len_begin_end = [1, 0, 0]
        def __record(idx, peer):
            idx_2_peers[idx].append(peer)
            idx_2_peer_set[idx].add(peer)
            length = idx - peer + 1
            if length > max_len_begin_end[0]:
                max_len_begin_end[:] = length, peer, idx

        for i, chr in enumerate(s[1:]):
            i = i + 1
            for j in chr_2_indexes[chr]:
                if j >= i:
                    break
                elif j + 1 == i:
                    __record(i, j)
                else:
                    prv_peer, prv = j+1, i-1
                    if prv_peer in idx_2_peer_set[prv]:
                        __record(i, j)
        return s[max_len_begin_end[1]: max_len_begin_end[2] + 1]


def judge_equal(long, result, golden):
    if len(result) != len(golden):
        return False
    if result not in long:
        return False
    for i, j in zip(result, result[::-1]):
        if i != j:
            return False
    return True


if __name__ == '__main__':
    test_cases = [
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('a', 'a'),
        ('ac', 'a'),
    ]
    s = Solution()
    for case in test_cases:
        long, golden = case
        result = s.longestPalindrome(long)
        print('long: {}, golden: {}, result: {}'.format(long, golden, result))
        assert judge_equal(long, result, golden)
