from collections import Counter
from typing import List

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#
#         i, j = 0, len(nums) - 1
#         count = 0
#         while i < len(nums):
#             is_found = False
#             look = k - nums[i]
#             if look <= 0:
#                 i += 1
#                 j = len(nums) - 1
#                 continue
#             while i < j:
#                 if nums[j] == look:
#                     nums.pop(j)
#                     nums.pop(i)
#                     count += 1
#                     is_found = True
#                     break
#                 j -= 1
#             if is_found:
#                 i, j = 0, len(nums) - 1
#             else:
#                 i+=1
#                 j = len(nums) - 1
#         return count

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        output = 0
        seen = set()
        for x in c:
            if x not in seen and (k-x) in c:
                if x == (k-x):
                    output += c[x]//2
                else:
                    output += min(c[x], c[k-x])
                seen.add(x)
                seen.add(k-x)
        return output


sol = Solution()
print(sol.maxOperations(nums=[2,2,2,3,1,1,4,1], k=4))



