#    Given two integer arrays of equal length target and arr.
#
#    In one step, you can select any non-empty sub-array of arr and reverse it.
#    You are allowed to make any number of steps.
#
#    Return True if you can make arr equal to target, or False otherwise.


class Solution:
    def canBeEqual(self, target, arr):
        return sorted(target) == sorted(arr)


if __name__ == "__main__":
    testinput1 = [1, 2, 3, 4]
    testinput2 = [2, 4, 1, 3]
    print(Solution.canBeEqual(Solution, testinput1, testinput2))
