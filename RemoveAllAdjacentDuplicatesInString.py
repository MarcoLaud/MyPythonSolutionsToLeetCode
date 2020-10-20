#    Given a string S of lowercase letters, a duplicate removal consists
#    of choosing two adjacent and equal letters, and removing them.
#
#    We repeatedly make duplicate removals on S until we no longer can.
#
#    Return the final string after all such duplicate removals have been made.
#    It is guaranteed the answer is unique.


class Solution:
    def removeDuplicates(self, S):
        s = []
        for lett in S:
            s.append(lett)
            if len(s) > 1 and s[~0] == s[~1]:
                s.pop()
                s.pop()
        return "".join(s)


if __name__ == "__main__":
    testinput = "abbaca"
    print(Solution.removeDuplicates(Solution, testinput))
