#    Given an array of integers nums, sort the array in increasing
#    order based on the frequency of the values. If multiple values
#    have the same frequency, sort them in decreasing order.
#
#    Return the sorted array.


class Solution:
    def frequencySort(self, nums):
        dic = {}
        res = []

        for num in set(nums):
            if nums.count(num) in dic:
                dic[nums.count(num)] = dic[nums.count(num)] + [num]
            else:
                dic[nums.count(num)] = [num]

        for freq in sorted(dic):
            for elem in sorted(dic[freq])[::-1]:
                res += [elem] * freq
        return(res)


if __name__ == '__main__':
    testinput = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(Solution.frequencySort(Solution, testinput))
