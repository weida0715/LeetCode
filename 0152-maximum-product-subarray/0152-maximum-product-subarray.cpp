class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int maxProduct = nums[0];
        int minProduct = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] >= 0) {
                maxProduct = max(nums[i], nums[i] * maxProduct);
                minProduct = min(nums[i], nums[i] * minProduct);
            } else {
                int temp = maxProduct;
                maxProduct = max(nums[i], nums[i] * minProduct);
                minProduct = min(nums[i], nums[i] * temp);
            }

            result = max(result, maxProduct);
        }

        return result;
    }
};