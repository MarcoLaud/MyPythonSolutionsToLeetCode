#    Given a string S and a character C, return an array of integers
#    representing the shortest distance from the character C in the string.


class Solution:
    def shortestToChar(self, S, C):
        res = []
        buffer = []
        indeces = [ii for ii in range(len(S)) if S[ii] == C]
        for ii in range(len(S)):
            for jj in map(lambda x: x - ii, indeces):
                buffer.append(abs(jj))
            res.append(min(buffer))
            buffer = []
        return res


if __name__ == "__main__":
    testinput1 = "marcoseibellissimo"
    testinput2 = 'o'
    print(Solution.shortestToChar(Solution, testinput1, testinput2))
