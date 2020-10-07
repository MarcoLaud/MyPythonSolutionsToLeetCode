#    Given an array of numbers arr. A sequence of numbers is called
#    an arithmetic progression if the difference between any two
#    consecutive elements is the same.
#
#    Return true if the array can be rearranged to form an
#    arithmetic progression, otherwise, return false.


class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr_sort = sorted(arr)
        diff = arr_sort[1] - arr_sort[0]
        return arr_sort == [arr_sort[0] + (nn - 1) * diff
                            for nn in range(1, len(arr)+1)]


if __name__ == "__main__":
    testinput = [2, 10, 7, 8, 3]
    print(Solution.canMakeArithmeticProgression(Solution, testinput))
