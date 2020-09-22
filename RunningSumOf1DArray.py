# Given an array nums.
# We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.


class Solution:
    def runningSum(self, nums):
        return [sum(nums[:ii+1]) for ii in range(len(nums))]