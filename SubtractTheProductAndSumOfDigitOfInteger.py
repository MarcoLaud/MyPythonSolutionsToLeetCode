#    Given an integer number n, return the difference between the product
#    of its digits and the sum of its digits.


class Solution:
    def subtractProductAndSum(self, n):
        pr = 1
        su = 0
        for elem in str(n):
            pr *= int(elem)
            su += int(elem)
        return pr - su

# Beats 18.20% and 38.30% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
