class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currIndex = 0

        for num in nums:
            if num != nums[currIndex]:
                currIndex += 1
                nums[currIndex] = num
        
        return currIndex + 1