#    Given an array A of strings made only from lowercase letters,
#    return a list of all characters that show up in all strings within
#    the list (including duplicates).  For example, if a character
#    occurs 3 times in all strings but not 4 times, you need to include
#    that character three times in the final answer.
#
#    You may return the answer in any order.


class Solution:
    def commonChars(self, A):
        uniques = set("".join([elem for elem in A]))
        occ = []
        for letter in uniques:
            freqs = []
            for elem in A:
                freqs.append(elem.count(letter))
            occ.append(min(freqs))
        return sum([[lett] * freq for lett, freq in zip(uniques, occ)
                    if occ != 0], [])


if __name__ == "__main__":
    testinput = ["bella", "label", "roller"]
    print(Solution.commonChars(Solution, testinput))
