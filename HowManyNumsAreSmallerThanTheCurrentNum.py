#    Given the array nums, for each nums[i] find out how many numbers
#    in the array are smaller than it. That is, for each nums[i] you have to
#    count the number of valid j's such that j != i and nums[j] < nums[i].
#
#    Return the answer in an array.


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        sorted_nums = sorted(nums)

        for ii, num in enumerate(sorted_nums):
            if num not in dic:
                dic[num] = ii
        return [dic[num] for num in nums]


if __name__ == '__main__':
    test_input = [8, 1, 2, 2, 3]
    print(Solution.smallerNumbersThanCurrent(Solution, test_input))
