#    Given the array of integers nums, you will choose two different
#    indices i and j of that array. Return the maximum value of
#    (nums[i]-1)*(nums[j]-1).


class Solution:
    def maxProduct(self, nums):
        return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] - 1)


if __name__ == "__main__":
    test_input = [3, 4, 5, 2]
    print(Solution.maxProduct(Solution, test_input))
