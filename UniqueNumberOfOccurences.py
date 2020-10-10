#    Given an array of integers arr, write a function that returns true
#    if and only if the number of occurrences of each value in the array
#    is unique.


class Solution:
    def uniqueOccurrences(self, arr):
        rec = [arr.count(elem) for elem in set(arr)]
        return len(rec) == len(set(rec))


if __name__ == "__main__":
    testinput = [1, 2, 2, 1, 1, 3]
    print(Solution.uniqueOccurrences(Solution, testinput))
