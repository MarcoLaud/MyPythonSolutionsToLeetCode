#    A valid parentheses string is either empty (""), "(" + A + ")",
#    or A + B, where A and B are valid parentheses strings,
#    and + represents string concatenation.
#
#    For example, "", "()", "(())()", and "(()(()))"
#    are all valid parentheses strings.
#
#    A valid parentheses string S is primitive if it is nonempty,
#    and there does not exist a way to split it into S = A+B,
#    with A and B nonempty valid parentheses strings.
#
#    Given a valid parentheses string S, consider its primitive
#    decomposition: S = P_1 + P_2 + ... + P_k,
#    where P_i are primitive valid parentheses strings.
#
#    Return S after removing the outermost parentheses
#    of every primitive string in the primitive decomposition of S.


class Solution:
    def removeOuterParentheses(self, S):
        count = 0
        res = ""
        first = 0
        for ii, par in enumerate(S):
            if par == '(':
                count += 1
            if par == ')':
                count -= 1
            if count == 0:
                res += S[first+1:ii]
                first = ii + 1
        return res


if __name__ == '__main__':
    test_input = "(()())(())"
    print(Solution.removeOuterParentheses(Solution, test_input))
