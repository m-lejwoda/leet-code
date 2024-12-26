from typing import List

#
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(len(numbers)-1, i, -1):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1, j+1]
#                 if numbers[i] + numbers[j] < target:
#                     break
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if numbers and len(numbers)>=2:
            start=0
            end=len(numbers)-1

            while start < end:
                sum = numbers[start]+numbers[end]

                if sum < target:

                    start=start+1
                elif sum > target:

                    end=end-1
                elif sum==target:
                    return [start+1, end+1]
s = Solution()
print(s.twoSum(numbers = [2,7,11,15], target = 9))
print(s.twoSum(numbers = [2,3,4], target = 6))
print(s.twoSum(numbers = [-1,0], target = -1))
