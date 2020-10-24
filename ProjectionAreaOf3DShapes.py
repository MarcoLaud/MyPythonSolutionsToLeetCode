#    On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned
#    with the x, y, and z axes.
#
#    Each value v = grid[i][j] represents a tower of v cubes placed on top
#    of grid cell (i, j).
#
#    Now we view the projection of these cubes onto the xy, yz, and zx planes.
#
#    A projection is like a shadow, that maps our 3 dimensional figure
#    to a 2 dimensional plane.
#
#    Here, we are viewing the "shadow" when looking at the cubes from
#    the top, the front, and the side.
#
#    Return the total area of all three projections.


class Solution:
    def projectionArea(self, grid):
        tot = len(grid[0]) ** 2
        tot -= sum([elem for elem in grid], []).count(0)
        for elem in grid:
            tot += max(elem)
        for elem in zip(*grid):
            tot += max(elem)
        return tot


if __name__ == "__main__":
    testinput = [[1, 2], [3, 4]]
    print(Solution.projectionArea(Solution, testinput))
