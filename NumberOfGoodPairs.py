#    Given an array of integers nums.
#
#    A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
#    Return the number of good pairs.


class Solution:
    def numIdenticalPairs(self, nums):
        hashMap = {}
        for elem in nums:
            if elem in hashMap:
                hashMap[elem] += 1
            else:
                hashMap[elem] = 1
        return hashMap


# beats 82.95% of Python 3 submission (2020/09/22)
