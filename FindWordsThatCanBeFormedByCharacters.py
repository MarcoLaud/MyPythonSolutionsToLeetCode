#    You are given an array of strings words and a string chars.
#
#    A string is good if it can be formed by characters from chars
#    (each character can only be used once).
#
#    Return the sum of lengths of all good strings in words.


class Solution:
    def countCharacters(self, words, chars):
        res = 0
        for word in words:
            if all([word.count(word[ii]) <= chars.count(word[ii])
                    for ii in range(len(word))]):
                res += len(word)
        return res


if __name__ == "__main__":
    testinput1 = ["cat", "bt", "hat", "tree"]
    testinput2 = "atach"
    print(Solution.countCharacters(Solution, testinput1, testinput2))
