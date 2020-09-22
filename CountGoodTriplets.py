#    Given an array of integers arr, and three integers a, b and c.
#    You need to find the number of good triplets.
#
#    A triplet (arr[i], arr[j], arr[k]) is good
#    if the following conditions are true:
#
#    0 <= i < j < k < arr.length
#    |arr[i] - arr[j]| <= a
#    |arr[j] - arr[k]| <= b
#    |arr[i] - arr[k]| <= c
#
#    Where |x| denotes the absolute value of x.
#
#    Return the number of good triplets.


class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        res = 0
        for ii in range(0, len(arr) - 2):
            for jj in range(1, len(arr)-1):
                if abs(arr[ii] - arr[jj]) <= a:
                    for kk in range(2, len(arr)):
                        if abs(arr[jj] - arr[kk]) <= b and \
                           abs(arr[ii] - arr[kk]) <= c and ii < jj < kk:
                            res += 1
        return res

# Beats 61.56% of Python 3 submissions in memory resp.
# (2020/09/22)
