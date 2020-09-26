#    Given a positive integer num consisting only of digits 6 and 9.
#
#    Return the maximum number you can get by changing at most
#    one digit (6 becomes 9, and 9 becomes 6).


class Solution:
    def maximum69Number(self, num):
        for ii, digit in enumerate(str(num)):
            if digit == '6':
                power = len(str(num)) - ii - 1
                num = num + 3 * 10 ** power
                break
        return num


if __name__ == '__main__':
    test_input = 969669
    print(Solution.maximum69Number(Solution, test_input))
