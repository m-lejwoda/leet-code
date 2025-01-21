from math import sqrt

# Try Binary
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        pass
        # if int(sqrt(num)) == sqrt(num):
        #     return True
        # return False


# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         if int(sqrt(num)) == sqrt(num):
#             return True
#         return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            middle = (l + r) // 2
            if (middle * middle) == num:
                return True
            elif (middle * middle) < num:
                l = middle + 1
            else:
                r = middle - 1
        return False

s = Solution()
s.isPerfectSquare(100)