#    Given a string s and an integer array indices of the same length.
#
#    The string s will be shuffled such that the character at the
#    ith position moves to indices[i] in the shuffled string.
#
#    Return the shuffled string.


class Solution:
    def restoreString(self, s, indices):
        return ''.join(s[indices.index(ii)] for ii in range(len(s)))


# Beats 26.53% and 93.81% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
