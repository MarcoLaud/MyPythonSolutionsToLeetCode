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


if __name__ == '__main__':
    test_input1 = 4
    test_input2 = 3
    print(Solution.xorOperation(Solution, test_input1, test_input2))
