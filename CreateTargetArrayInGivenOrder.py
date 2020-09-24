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


if __name__ == '__main__':
    test_input1 = [1, 2, 3, 4, 0]
    test_input2 = [0, 1, 2, 3, 0]
    print(Solution.createTargetArray(Solution, test_input1, test_input2))
