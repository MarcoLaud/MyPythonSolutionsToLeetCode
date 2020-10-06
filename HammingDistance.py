#    The Hamming distance between two integers is the number of positions
#    at which the corresponding bits are different.
#
#    Given two integers x and y, calculate the Hamming distance.
#
#    Note:
#    0 ≤ x, y < 2^31.


class Solution:
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    testinput1 = 1
    testinput2 = 4
    print(Solution.hammingDistance(Solution, testinput1, testinput2))
