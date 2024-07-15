from typing import List


class Solution:
    def profit_transaction(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit

sol = Solution()
print(sol.profit_transaction([2,3,1,1,4]))