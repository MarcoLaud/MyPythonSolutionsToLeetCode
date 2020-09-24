#    Given a string s and an integer array indices of the same length.
#
#    The string s will be shuffled such that the character at the
#    ith position moves to indices[i] in the shuffled string.
#
#    Return the shuffled string.


class Solution:
    def restoreString(self, s, indices):
        return ''.join(s[indices.index(ii)] for ii in range(len(s)))


if __name__ == '__main__':
    test_input1 = "aaiougrt"
    test_input2 = [4, 0, 2, 6, 7, 3, 1, 5]
    print(Solution.restoreString(Solution, test_input1, test_input2))
