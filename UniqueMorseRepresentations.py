#    International Morse Code defines a standard encoding where each
#    letter is mapped to a series of dots and dashes, as follows:
#    "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.",
#    and so on.


class Solution:
    def uniqueMorseRepresentations(self, words):
        dic = {}
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                 "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                 "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                 "-.--", "--.."]
        new_words = ["" for ii in range(len(words))]

        for ii in range(26):                # dictionary
            dic[chr(ii+97)] = morse[ii]

        for ii, word in enumerate(words):
            for letter in word:
                new_words[ii] += dic[letter]
        return len(set(new_words))


if __name__ == "__main__":
    test_input = ["gin", "zen", "gig", "msg"]
    print(Solution.uniqueMorseRepresentations(Solution, test_input))
