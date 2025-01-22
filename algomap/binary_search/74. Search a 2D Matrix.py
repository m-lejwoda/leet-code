from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            middle = (top + bottom) // 2
            middle_row = matrix[middle]
            if middle_row[0] <= target and middle_row[len(middle_row)-1] >= target:
                l,r = 0, len(middle_row) -1
                while l <= r:
                    m = (l+r) // 2
                    if middle_row[m] == target:
                        return True
                    elif middle_row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False

            elif middle_row[0] <= target:
                top = middle + 1
            else:
                bottom = middle - 1
        return False







s = Solution()
# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
# print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
# print(s.searchMatrix([[1]],0))
print(s.searchMatrix([[1],[3]],2))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))