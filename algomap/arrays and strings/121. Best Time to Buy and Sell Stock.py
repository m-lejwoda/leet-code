from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        left, right = 0, 1
        max_profit = 0
        while right < length:
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit

s= Solution()
print(s.maxProfit([7,1,5,3,6,4]))
