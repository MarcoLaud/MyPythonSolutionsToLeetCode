#    Given an array of unique integers salary where salary[i] is the salary
#    of the employee i.
#
#    Return the average salary of employees excluding the
#    minimum and maximum salary.


class Solution:
    def average(self, salary):
        return sum(sorted(salary)[1:len(salary)-1]) / (len(salary) - 2)


if __name__ == "__main__":
    testinput = [4000, 3000, 1000, 2000]
    print(Solution.average(Solution, testinput))
