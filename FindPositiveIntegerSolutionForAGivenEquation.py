#    Given a function  f(x, y) and a value z, return all positive integer
#    pairs x and y where f(x,y) == z.
#
#    The function is constantly increasing, i.e.:
#
#    f(x, y) < f(x + 1, y)
#    f(x, y) < f(x, y + 1)
#    The function interface is defined like this:
#
#    interface CustomFunction {
#    public:
#      // Returns positive integer f(x, y) for any given
#      // positive integer x and y.
#
#      int f(int x, int y);
#    };
#    For custom testing purposes you're given an integer function_id
#    and a target z as input, where function_id represent one function
#    from an secret internal list, on the examples you'll know only
#    two functions from the list.
#
#    You may return the solutions in any order.
#
#    Constraints:
#
#    1 <= function_id <= 9
#    1 <= z <= 100
#    It's guaranteed that the solutions of f(x, y) == z will be
#    on the range 1 <= x, y <= 1000
#    It's also guaranteed that f(x, y) will fit in 32 bit signed integer
#    if 1 <= x, y <= 1000


class Solution:
    def findSolution(self, customfunction, z):
        res = []
        for xx in range(1, z+1):
            left = 1
            right = z + 1
            while left < right:
                mid = (left + right) // 2
                if customfunction(xx, mid) == z:
                    res.append([xx, mid])
                if customfunction(xx, mid) > z:
                    right = mid
                else:
                    left = mid + 1
        return res


if __name__ == "__main__":
    def f(x, y): return x + y
    testinput = 5
    print(Solution.findSolution(Solution, f, testinput))
