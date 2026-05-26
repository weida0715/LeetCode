class Solution {
    public int removeDuplicates(int[] nums) {
        int currNum = nums[0];
        int unique = 1;

        for (int i = 1; i < nums.length; i++) {
            if (currNum != nums[i]) {
                currNum = nums[i];
                nums[unique] = currNum;
                unique++;
            }
        }

        return unique;
    }
}