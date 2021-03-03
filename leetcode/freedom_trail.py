import string
import pdb

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(ring), len(key)
        dt = self.dist_table(m)
        dp = [[0 for _ in range(n+1)] for _ in range(m)]
        # dp[i][j]: if ring points to i, how many steps should take to satisfy key[j:]
        for j in range(n):
            j = n - 1 - j
            for i in range(m):
                dp[i][j] = min([dp[k][j+1] + dt[i][k] for k in range(m) if ring[k] == key[j]])
        return dp[0][0]


    def findRotateStepsBak(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        dt = self.dist_table(n)
        char_to_indexes = self.get_char_to_indexes(ring)
        next_char_dist = self.get_next_char_dist(ring, dt, char_to_indexes)
        pool = [(0, 0)]
        n_steps = self.bfs(ring, next_char_dist, key, 0, pool, 0)
        return n_steps

    def bfs(self, ring, next_char_dist, key, depth, pool, shortest):
        if depth == len(key):
            return shortest
        new_pool = []
        new_shortest = (len(ring) // 2 + 1) * len(key)
        new_up_bound = new_shortest
        for pointer, trail in pool:
            target_dist = next_char_dist[pointer][key[depth]]
            for target, dist in target_dist:
                new_trail = trail + dist
                if new_trail < new_shortest:
                    new_shortest = new_trail
                    new_up_bound = new_shortest + (len(key) - depth - 1) * (len(ring) // 2 + 1)
                if new_trail <= new_up_bound:
                    new_pool.append((target, new_trail))
        return self.bfs(ring, next_char_dist, key, depth+1, new_pool, new_shortest)

    def get_char_to_indexes(self, ring):
        char_to_indexes = {}
        for i, char in enumerate(ring):
            if char not in char_to_indexes:
                char_to_indexes[char] = [i]
            else:
                char_to_indexes[char].append(i)
        return char_to_indexes

    def get_next_char_dist(self, ring, dt, char_to_indexes):
        next_char_dist = [{} for _ in range(len(ring))]
        for i, _ in enumerate(ring):
            for char, indexes in char_to_indexes.items():
                next_char_dist[i][char] = [(j, dt[i][j]) for j in indexes]
        return next_char_dist

    def dist_table(self, n):
        table = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist = abs(i - j)
                if dist > n // 2:
                    dist = n - dist
                table[i][j] = dist + 1  # 1 stands for button
        return table

if __name__ == '__main__':
    s = Solution()
    steps = s.findRotateSteps('godding', 'gd')
    print(steps)
