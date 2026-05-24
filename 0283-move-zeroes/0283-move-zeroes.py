class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                temp = nums[k]
                nums[k] = num
                nums[i] = temp
                k += 1