#    Given two arrays of integers nums and index. Your task is to create
#    target array under the following rules:
#
#    Initially target array is empty.
#
#    From left to right read nums[i] and index[i], insert at index index[i]
#    the value nums[i] in target array.
#
#    Repeat the previous step until there are no elements to read
#    in nums and index.
#
#    Return the target array.


class Solution:
    def createTargetArray(self, nums, index):
        arr = []
        for ii, ind in enumerate(index):
            arr.insert(ind, nums[ii])
        return arr

# Beats 76.09% and 82.47% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
