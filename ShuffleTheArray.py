#    Given the array nums consisting of 2n elements in the form
#
#    [x1,x2,...,xn,y1,y2,...,yn].
#
#    Return the array in the form [x1,y1,x2,y2,...,xn,yn].


class Solution:
    def shuffle(self, nums, n):
        return nums if [nums.insert((n - i), nums.pop())
                        for i in range(n)] != 0 else None


if __name__ == '__main__':
    test_input1 = [1, 2, 3, 4, 4, 3, 2, 1]
    test_input2 = 4
    print(Solution.shuffle(Solution, test_input1, test_input2))
