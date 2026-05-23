class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num >= 0:
                maxProduct = max(num, num * maxProduct)
                minProduct = min(num, num * minProduct)
            else:
                temp = maxProduct
                maxProduct = max(num, num * minProduct)
                minProduct = min(num, num * temp)
            
            result = max(result, maxProduct)

        return result 