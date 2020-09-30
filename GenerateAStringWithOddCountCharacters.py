#    Given an integer n, return a string with n characters such that
#    each character in such string occurs an odd number of times.
#
#    The returned string must contain only lowercase English letters.
#    If there are multiples valid strings, return any of them.


class Solution:
    def generateTheString(self, n):
        return ('a' * (n-1)) + ('a' * (n % 2)) + ('b' * ((n % 2) ^ 1))


if __name__ == "__main__":
    testinput = 8
    print(Solution.generateTheString(Solution, testinput))
