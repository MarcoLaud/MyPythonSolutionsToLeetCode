#    Given two integer arrays startTime and endTime and
#    given an integer queryTime.
#
#    The ith student started doing their homework at the time
#    startTime[i] and finished it at time endTime[i].
#
#    Return the number of students doing their homework
#    at time queryTime. More formally, return the number of students
#    where queryTime lays in the interval
#    [startTime[i], endTime[i]] inclusive.


class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        studs = 0
        for ii in range(len(startTime)):
            if startTime[ii] <= queryTime <= endTime[ii]:
                studs += 1
        return studs


if __name__ == "__main__":
    test_input1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_input2 = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    query = 5
    print(Solution.busyStudent(Solution, test_input1, test_input2, query))
