#    Given n and m which are the dimensions of a matrix initialized
#    by zeros and given an array indices where indices[i] = [ri, ci].
#    For each pair of [ri, ci] you have to increment
#    all cells in row ri and column ci by 1.
#
#    Return the number of cells with odd values in the matrix
#    after applying the increment to all indices.


class Solution:
    def oddCells(self, n, m, indices):
        matr = [[0 for ii in range(m)] for jj in range(n)]  # Null matrix

        for elem in indices:
            for ii in range(m):
                matr[elem[0]][ii] += 1
            for jj in range(n):
                matr[jj][elem[1]] += 1

        return sum(elem % 2 for row in matr for elem in row)


if __name__ == "__main__":
    test_input = [[0, 1], [1, 1]]
    n = 2
    m = 3
    print(Solution.oddCells(Solution, n, m, test_input))
