#    Given a m * n matrix mat of ones (representing soldiers) and zeros
#    (representing civilians), return the indexes of the k weakest rows
#    in the matrix ordered from the weakest to the strongest.
#
#    A row i is weaker than row j, if the number of soldiers in row i is
#    less than the number of soldiers in row j, or they have the same number
#    of soldiers but i is less than j. Soldiers are always stand in the
#    frontier of a row, that is, always ones may appear first and then zeros.


class Solution:
    def kWeakestRows(self, mat, k):
        arr = []
        for ii, row in enumerate(mat):
            arr.append([sum(row), ii])
        return [couple[1] for couple in sorted(arr)[:k]]


if __name__ == "__main__":
    testinput1 = [[1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 0],
                  [1, 0, 0, 0, 0],
                  [1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 1]]
    testinput2 = 3
    print(Solution.kWeakestRows(Solution, testinput1, testinput2))
