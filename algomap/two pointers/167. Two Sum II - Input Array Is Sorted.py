from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum(numbers = [2,3,4], target = 6))
print(s.twoSum(numbers = [-1,0], target = -1))