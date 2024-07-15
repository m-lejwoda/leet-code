from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        if len(flowerbed) < 3:
            if 1 in flowerbed:
                res = 0
            else:
                res += 1

        for i in range(1, len(flowerbed) - 1):
            if i == 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i - 1] = 1
                res += 1
            if i == len(flowerbed) - 2 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i + 1] = 1
                res += 1
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                res += 1
        if res >= n:
            return True
        return False
