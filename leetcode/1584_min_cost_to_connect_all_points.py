class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return 0
        x_lst = sorted(list(set([p[0] for p in points])))
        x_to_idx = {x: i for i, x in enumerate(x_lst)}
        y_lst = sorted(list(set([p[1] for p in points])))
        points_x_y = self.sort_by_x_then_by_y(points, x_lst, x_to_idx)
        for x_idx, points_at_x in enumerate(points_x_y):
            for y_idx, point in enumerate(points_at_x):
                x, y = point
                almost = self.find_almost_near(x_idx, y_idx, points_x_y)
                min_dist = self._dist(point, almost)
                xx_idx = x_idx
                while xx_idx >= 0 and x_lst[xx_idx] + min_dist > x:
                    xx_point = self.find_near_on_xx(x_idx, y_idx, points_x_y, xx_idx)
                    dist = self._dist(point, xx_point)
                    if dist < min_dist:
                        min_dist = dist
                    xx_idx -= 1
                xx_idx = x_idx
                while xx_idx < len(x_lst) and x_lst[xx_idx] < min_dist + x:
                    xx_point = self.find_near_on_xx(x_idx, y_idx, points_x_y, xx_idx)
                    dist = self._dist(point, xx_point)
                    if dist < min_dist:
                        min_dist = dist
                    xx_idx += 1

    def sort_by_x_then_by_y(self, points, x_lst, x_to_idx):
        result = [list() for _ in x_lst]
        for p in points:
            x_idx = x_to_idx[p[0]]
            result[x_idx].append(p)
        for i, points_at_x in enumerate(result):
            result[i] = sorted(points_at_x, key=lambda p: p[1])
        return result

    def find_almost_near(self, x_idx, y_idx, points_x_y):
        point = points_x_y[x_idx][y_idx]
        x, y = point
        almost, almost_dist = None, None
        if x_idx > 0:
            left_x_idx = x_idx - 1
            left_y_idx = self.find_nearest_y(points_x_y[left_x_idx], y)
            left_point = points_x_y[left_x_idx, left_y_idx]
            dist = self._dist(point, left_point)
            if almost_dist is None or dist < almost_dist:
                almost, almost_dist = left_point, dist
        if x_idx < len(points_x_y) - 1:
            right_x_idx = x_idx + 1
            right_y_idx = self.find_nearest_y(points_x_y[right_x_idx], y)
            right_point = points_x_y[right_x_idx][right_y_idx]
            dist = self._dist(point, right_point)
            if almost_dist is None or dist < almost_dist:
                almost, almost_dist = right_point, dist
        if y_idx > 0:
            down_y_idx = y_idx - 1
            down_point = points_x_y[x_idx][down_y_idx]
            dist = self._dist(point, down_point)
            if almost_dist is None or dist < almost_dist:
                almost, almost_dist = down_point, dist
        if y_idx < len(points_x_y[x_idx]) - 1:
            up_y_idx = y_idx + 1
            up_point = points_x_y[x_idx][up_y_idx]
            dist = self._dist(point, up_point)
            if almost_dist is None or dist < almost_dist:
                almost, almost_dist = up_point, dist
        return almost

    def _dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



