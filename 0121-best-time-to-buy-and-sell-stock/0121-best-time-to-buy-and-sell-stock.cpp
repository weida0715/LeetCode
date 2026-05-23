class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSoFar = prices[0];
        int ans = 0;

        for (int i = 1; i < prices.size(); i++) {
            int profit = prices[i] - minSoFar;
            if (profit > ans) {
                ans = profit;
            }

            minSoFar = min(prices[i], minSoFar);
        }

        return ans;
    }
};