class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            profit = prices[i] - minSoFar
            if profit > ans:
                ans = profit

            minSoFar = min(prices[i], minSoFar)

        return ans
        