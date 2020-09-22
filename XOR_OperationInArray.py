#    Given an integer n and an integer start.
#
#    Define an array nums where
#
#    nums[i] = start + 2*i (0-indexed) and n == nums.length.
#
#    Return the bitwise XOR of all elements of nums.


from functools import reduce


class Solution:
    def xorOperation(self, n, start):
        nums = [start + 2 * ii for ii in range(n)]
        return reduce(lambda x, y: x ^ y, nums)

# Beats 79.58% and 32.59% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
