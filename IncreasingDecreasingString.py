#    Given a string s. You should re-order the string using
#    the following algorithm:
#
#    Pick the smallest character from s and append it to the result.
#    Pick the smallest character from s which is greater than the
#    last appended character to the result and append it.
#    Repeat step 2 until you cannot pick more characters.
#    Pick the largest character from s and append it to the result.
#    Pick the largest character from s which is smaller than the
#    last appended character to the result and append it.
#    Repeat step 5 until you cannot pick more characters.
#    Repeat the steps from 1 to 6 until you pick all characters from s.
#    In each step, If the smallest or the largest character appears
#    more than once you can choose any occurrence and
#    append it to the result.
#
#    Return the result string after sorting s with this algorithm.


class Solution:
    def sortString(self, s):
        listed_string = list(s)
        listed_uniques = list(set(s))
        listed_uniques.sort()
        result = ''

        while listed_string != [''] * len(s):
            for elem in listed_uniques:
                result = result + elem
                listed_string[listed_string.index(elem)] = ''
            listed_uniques = list(set(listed_string))
            listed_uniques.sort()
            for elem in listed_uniques[::-1]:
                result = result + elem
                listed_string[listed_string.index(elem)] = ''
            listed_uniques = list(set(listed_string))
            listed_uniques.sort()
        return result


if __name__ == "__main__":
    testinput = "leetcode"
    print(Solution.sortString(Solution, testinput))
