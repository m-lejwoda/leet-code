from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            min_value = min(height[i], height[j])
            if result < (j - i) * min_value:
                result = (j - i) * min_value
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result
