#    On a plane there are n points with integer coordinates
#
#    points[i] = [xi, yi].
#
#    Your task is to find the minimum time in seconds to visit all points.
#
#    You can move according to the next rules:
#
#    In one second always you can either move vertically, horizontally
#    by one unit or diagonally (it means to move one unit vertically
#    and one unit horizontally in one second).
#
#    You have to visit the points in the same order as they appear
#    in the array.


class Solution:
    def minTimeToVisitAllPoints(self, points):
        t = 0
        dists = [[abs(points[ii][0] - points[ii+1][0]),
                  abs(points[ii][1] - points[ii+1][1])]
                 for ii in range(len(points)-1)]

        mins = [min(dists[ii][0], dists[ii][1]) for ii in range(len(dists))]

        for ii in range(len(dists)):
            dists[ii] = [dists[ii][0] - mins[ii], dists[ii][1] - mins[ii]]
            t += mins[ii]

        for ii in range(len(dists)):
            t += sum(dists[ii])
        return t

# Beats 78.71% and 47.46% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
