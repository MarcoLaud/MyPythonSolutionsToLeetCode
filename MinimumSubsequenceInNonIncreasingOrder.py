#    Given the array nums, obtain a subsequence of the array
#    whose sum of elements is strictly greater than the sum of
#    the non included elements in such subsequence.
#
#    If there are multiple solutions, return the subsequence with
#    minimum size and if there still exist multiple solutions,
#    return the subsequence with the maximum total sum of all its elements.
#    A subsequence of an array can be obtained by erasing some (possibly zero)
#    elements from the array.
#
#    Note that the solution with the given constraints is guaranteed
#    to be unique. Also return the answer sorted in non-increasing order.


class Solution:
    def minSubsequence(self, nums):
        ssnums = sorted(nums, reverse=True)
        for ii in range(len(nums)):
            if sum(ssnums[:ii+1]) > sum(ssnums[ii+1:]):
                return ssnums[:ii+1]
                break


if __name__ == "__main__":
    testinput = [4, 3, 10, 9, 8]
    print(Solution.minSubsequence(Solution, testinput))
