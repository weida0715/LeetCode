class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null | nums.length == 0) {
            return 0;
        }

        int maxProduct = nums[0];
        int minProduct = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] >= 0) {
                maxProduct = Math.max(nums[i], nums[i] * maxProduct);
                minProduct = Math.min(nums[i], nums[i] * minProduct);
            } else {
                int temp = maxProduct;
                maxProduct = Math.max(nums[i], nums[i] * minProduct);
                minProduct = Math.min(nums[i], nums[i] * temp);
            }

            result = Math.max(result, maxProduct);
        }

        return result;
    }
}