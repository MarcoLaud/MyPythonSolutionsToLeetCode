#    The Fibonacci numbers, commonly denoted F(n) form a sequence,
#    called the Fibonacci sequence, such that each number is the sum of
#    the two preceding ones, starting from 0 and 1. That is,
#
#    F(0) = 0,   F(1) = 1
#    F(N) = F(N - 1) + F(N - 2), for N > 1.
#
#    Given N, calculate F(N).


class Solution:
    def fib(self, N):
        phi = round((1 + 5 ** 0.5) / 2, 4)
        return round((phi ** N - (-phi) ** (-N)) / (5 ** 0.5))


if __name__ == "__main__":
    testinput = 4
    print(Solution.fib(Solution, testinput))
