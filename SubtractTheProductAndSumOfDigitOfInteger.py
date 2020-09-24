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


if __name__ == '__main__':
    test_input = 4421
    print(Solution.subtractProductAndSum(Solution, test_input))
