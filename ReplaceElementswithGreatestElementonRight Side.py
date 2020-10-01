#    Given an array arr, replace every element in that array
#    with the greatest element among the elements to its right,
#    and replace the last element with -1.
#
#    After doing so, return the array.


class Solution:
    def replaceElements(self, arr):
        maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            last = maxNum
            maxNum = max(maxNum, arr[i])
            arr[i] = last
        return arr


if __name__ == "__main__":
    testinput = [17, 18, 5, 4, 6, 1]
    print(Solution.replaceElements(Solution, testinput))

# Solution by game123web
