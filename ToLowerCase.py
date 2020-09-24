#    Implement function ToLowerCase() that has a string parameter str,
#    and returns the same string in lowercase.


class Solution:
    def toLowerCase(self, s) -> str:
        return s.lower()


if __name__ == '__main__':
    test_input = 'HelLo'
    print(Solution.toLowerCase(Solution, test_input))
