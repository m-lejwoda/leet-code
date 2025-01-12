from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        max_area = 0
        while l<r:
            temp_min = min(height[l],height[r])
            max_area = max(max_area,temp_min * (r-l))
            if height[l]<=height[r]:
                l+=1
                continue
            else:
                r-=1
                continue
        return max_area



s = Solution()
print(s.maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))