#    Given a string, you need to reverse the order of characters in each
#    word within a sentence while still preserving whitespace
#    and initial word order.


class Solution:
    def reverseWords(self, s):
        return " ".join([word[::-1] for word in s.split()])


if __name__ == "__main__":
    testinput = "Let's take LeetCode contest"
    print(Solution.reverseWords(Solution, testinput))
