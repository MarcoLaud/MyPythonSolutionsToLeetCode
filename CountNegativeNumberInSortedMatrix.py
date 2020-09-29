#    Given a m * n matrix grid which is sorted in non-increasing order
#    both row-wise and column-wise.
#
#    Return the number of negative numbers in grid.


class Solution:
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for elem in row[::-1]:
                if elem < 0:
                    count += 1
                else:
                    break
        return count


if __name__ == "__main__":
    testinput = [[4, 3, 2, -1], [3, 2, 1, -1],
                 [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(Solution.countNegatives(Solution, testinput))
