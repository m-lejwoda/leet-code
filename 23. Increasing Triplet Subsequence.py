from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        smallest = next_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= next_smallest:
                next_smallest = num
            else:
                return True
        return False
sol = Solution()
sol.increasingTriplet([2,3,1,3,2,4,3])