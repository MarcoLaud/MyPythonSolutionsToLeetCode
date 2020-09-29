#    Given a string s formed by digits ('0' - '9') and '#' .
#    We want to map s to English lowercase characters as follows:
#
#    Characters ('a' to 'i') are represented by
#    ('1' to '9') respectively.
#    Characters ('j' to 'z') are represented by
#    ('10#' to '26#') respectively.
#    Return the string formed after mapping.
#
#    It's guaranteed that a unique mapping will always exist.


class Solution:
    def freqAlphabets(self, s):
        for ii in range(26, 0, -1):
            s = s.replace(str(ii) + '#'*(ii > 9), chr(ii+96))
        return s


if __name__ == "__main__":
    test_input = "10#11#12"
    print(Solution.freqAlphabets(Solution, test_input))

# Great solution by Junaid Mansuri
