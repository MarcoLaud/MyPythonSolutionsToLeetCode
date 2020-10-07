#    Given an array of integers A sorted in non-decreasing order,
#    return an array of the squares of each number,
#    also in sorted non-decreasing order.


class Solution:
    def sortedSquares(self, A):
        return sorted([num ** 2 for num in A])


if __name__ == "__main__":
    testinput = [-4, -1, 0, 3, 10]
    print(Solution.sortedSquares(Solution, testinput))
