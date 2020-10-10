#    Given a m * n matrix of distinct numbers, return all lucky numbers
#    in the matrix in any order.
#
#    A lucky number is an element of the matrix such that it is the
#    minimum element in its row and maximum in its column.


class Solution:
    def luckyNumbers(self, matrix):
        return set(min(row) for row in matrix) & \
                set(max(column) for column in zip(*matrix))


if __name__ == "__main__":
    testinput = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(Solution.luckyNumbers(Solution, testinput))
