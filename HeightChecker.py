#    Students are asked to stand in non-decreasing order of heights
#    for an annual photo.
#
#    Return the minimum number of students that must move in order
#    for all students to be standing in non-decreasing order of height.
#
#    Notice that when a group of students is selected they can reorder
#    in any possible way between themselves and the non selected students
#     remain on their seats.


class Solution:
    def heightChecker(self, heights):
        return sum(initial != target for initial, target
                   in zip(heights, sorted(heights)))


if __name__ == "__main__":
    testinput = [1, 1, 4, 2, 1, 3]
    print(Solution.heightChecker(Solution, testinput))
