#    Build the target array using the following operations:
#
#    Push: Read a new element from the beginning list,
#    and push it in the array.
#    Pop: delete the last element of the array.
#    If the target array is already built, stop reading more elements.
#    You are guaranteed that the target array is strictly increasing,
#    only containing numbers between 1 to n inclusive.
#
#    Return the operations to build the target array.
#
#    You are guaranteed that the answer is unique.


class Solution:
    def buildArray(self, target, n):
        res = []
        for ii in range(1, target[~0] + 1):
            if ii in target:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
        return res


if __name__ == "__main__":
    testinput1 = [1, 3]
    testinput2 = 3
    print(Solution.buildArray(Solution, testinput1, testinput2))
