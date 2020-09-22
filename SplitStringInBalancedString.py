#    Balanced strings are those who have equal quantity of
#    'L' and 'R' characters.
#
#    Given a balanced string s split it in the maximum amount of
#    balanced strings.
#
#    Return the maximum amount of splitted balanced strings.


class Solution:
    def balancedStringSplit(self, s):
        count = res = 0
        for lett in s:
            if lett == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += 1
        return res

# Beats 55.90% and 52.39% of Python 3 submissions in runtime and memory resp.
# (2020/09/22)
