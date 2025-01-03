from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_value = set()
        for num in nums:
            if num in set_value:
                return True
            else:
                set_value.add(num)
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,4,5]))
print(s.containsDuplicate(nums = [1,2,3,1]))
print(s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))