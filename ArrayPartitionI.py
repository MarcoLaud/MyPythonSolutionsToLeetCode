#    Given an array of 2n integers, your task is to group these integers
#    into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn)
#    which makes sum of min(ai, bi) for all i from 1 to n as large as possible.


class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    testinput = [1, 4, 3, 2]
    print(Solution.arrayPairSum(Solution, testinput))
