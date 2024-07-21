from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums_1 = set()
        set_nums_2 = set()
        for i in nums1:
            if i not in nums2:
                set_nums_1.add(i)
        for i in nums2:
            if i not in nums1:
                set_nums_2.add(i)
        return [list(set_nums_1), list(set_nums_2)]

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [nums1.difference(nums2),nums2.difference(nums1)]

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        res=[[],[]]

        for i in set1:
            if i not in set2:
                res[0].append(i)
        for i in set2:
            if i not in set1:
                res[1].append(i)
        return res
