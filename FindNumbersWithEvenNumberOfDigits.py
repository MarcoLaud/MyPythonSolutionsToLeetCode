#    Given an array nums of integers,
#    return how many of them contain an even number of digits.


class Solution:
    def findNumbers(self, nums):
        return len([n for n in nums if len(str(n)) % 2 == 0])


if __name__ == '__main__':
    test_input = [12, 345, 2, 6, 7896]
    print(Solution.findNumbers(Solution, test_input))
