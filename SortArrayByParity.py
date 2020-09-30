#    Given an array A of non-negative integers, return an array
#    consisting of all the even elements of A,
#    followed by all the odd elements of A.
#
#    You may return any answer array that satisfies this condition.


class Solution:
    def sortArrayByParity(self, A):
        return [even for even in A if (even % 2) ^ 1] + \
                [odd for odd in A if odd % 2]


if __name__ == "__main__":
    testinput = [3, 1, 2, 4]
    print(Solution.sortArrayByParity(Solution, testinput))
