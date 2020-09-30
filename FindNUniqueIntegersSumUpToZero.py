#    Given an integer n, return any array containing n unique integers
#    such that they add up to 0.


class Solution:
    def sumZero(self, n):
        arr = []
        index = (n + 2 - (1 * (n % 2))) // 2
        for ii in range(1, index):
            arr = arr + [ii] + [-ii]
        if n % 2:
            arr = arr + [0]
        return arr


if __name__ == "__main__":
    testinput = 5
    print(Solution.sumZero(Solution, testinput))
