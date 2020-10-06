#    In a array A of size 2N, there are N+1 unique elements,
#    and exactly one of these elements is repeated N times.
#
#    Return the element repeated N times.


class Solution:
    def repeatedNTimes(self, A):
        for elem in A:
            if A.count(elem) > 1:
                return elem
                break


if __name__ == "__main__":
    testinput = [1, 2, 3, 3]
    print(Solution.repeatedNTimes(Solution, testinput))
