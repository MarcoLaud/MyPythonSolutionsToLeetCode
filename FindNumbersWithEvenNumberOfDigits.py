#    Given an array nums of integers,
#    return how many of them contain an even number of digits.


class Solution:
    def findNumbers(self, nums):
        return len([n for n in nums if len(str(n)) % 2 == 0])

# Beats 98.86% and 14.22% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
