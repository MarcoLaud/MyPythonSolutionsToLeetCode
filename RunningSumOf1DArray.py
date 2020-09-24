# Given an array nums.
# We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.


class Solution:
    def runningSum(self, nums):
        return [sum(nums[:ii+1]) for ii in range(len(nums))]


if __name__ == '__main__':
    test_input = [3, 1, 2, 10, 1]
    print(Solution.runningSum(Solution, test_input))
