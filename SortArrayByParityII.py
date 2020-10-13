#    Given an array A of non-negative integers, half of the integers in A
#    are odd, and half of the integers are even.
#
#    Sort the array so that whenever A[i] is odd, i is odd;
#    and whenever A[i] is even, i is even.
#
#    You may return any answer array that satisfies this condition.


class Solution:
    def sortArrayByParityII(self, Arr):
        Even = []
        Odd = []
        for elem in Arr:
            if elem % 2 == 0:
                Even.append(elem)
            else:
                Odd.append(elem)
        return sum([[x, y] for x, y in zip(Even, Odd)], [])


if __name__ == "__main__":
    testinput = [4, 2, 5, 7]
    print(Solution.sortArrayByParityII(Solution, testinput))
