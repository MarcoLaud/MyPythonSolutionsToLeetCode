#    Given two arrays arr1 and arr2, the elements of arr2 are distinct,
#    and all elements in arr2 are also in arr1.
#
#    Sort the elements of arr1 such that the relative ordering of items
#    in arr1 are the same as in arr2.  Elements that don't appear in arr2
#    should be placed at the end of arr1 in ascending order.


class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr3 = []
        diff = set(arr1) - set(arr2)
        for elem in arr2:
            arr3 += [elem] * arr1.count(elem)
        for elem in sorted(diff):
            arr3 += [elem] * arr1.count(elem)
        return arr3


if __name__ == "__main__":
    testinput1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    testinput2 = [2, 1, 4, 3, 9, 6]
    print(Solution.relativeSortArray(Solution, testinput1, testinput2))
