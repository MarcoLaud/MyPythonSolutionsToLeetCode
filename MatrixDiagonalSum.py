#    Given a square matrix mat, return the sum of the matrix diagonals.
#
#    Only include the sum of all the elements on the primary diagonal
#    and all the elements on the secondary diagonal
#     that are not part of the primary diagonal.


class Solution:
    def diagonalSum(self, mat):
        from numpy import array, identity
        mat = array(mat)
        res = int(sum(sum(mat * identity(len(mat)))) +
                  sum(sum(mat * identity(len(mat))[::-1])))
        if len(mat) % 2 == 1:
            return res - mat[len(mat) // 2, len(mat) // 2]
        else:
            return res


if __name__ == '__main__':
    test_input = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    print(Solution.diagonalSum(Solution, test_input))
