class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        ans = 0

        for price in prices:
            ans = max(ans, price - minSoFar)
            minSoFar = min(price, minSoFar)

        return ans