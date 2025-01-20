from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1

        return -1
s= Solution()
print(s.search([-1,0,3,5,9,12], 5))
print(s.search([-1,0,3,5,9,12], 2))