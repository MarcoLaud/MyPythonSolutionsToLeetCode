#    A self-dividing number is a number that is divisible by
#    every digit it contains.
#
#    For example, 128 is a self-dividing number because
#    128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
#    Also, a self-dividing number is not allowed to contain the digit zero.
#
#    Given a lower and upper number bound, output a list of every possible
#    self dividing number, including the bounds if possible.


class Solution:
    def selfDividingNumbers(self, left, right):
        return [num for num in range(left, right + 1) if all([digit != '0' and
                num % int(digit) == 0 for digit in str(num)])]


if __name__ == "__main__":
    testinput1 = 1
    testinput2 = 22
    print(Solution.selfDividingNumbers(Solution, testinput1, testinput2))
