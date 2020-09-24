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


if __name__ == '__main__':
    test_input = [1, 2, 3, 1, 1, 3]
    print(Solution.numIdenticalPairs(Solution, test_input))
