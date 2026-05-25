class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mc = 0
        count = 0

        for num in nums:
            if count == 0:
                mc = num
            
            if num == mc:
                count += 1
            else:
                count -= 1

        return mc