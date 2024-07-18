from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        highest = 0
        for i in gain:
            res += i
            if res > highest:
                highest = res
        return highest