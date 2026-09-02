class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        smaller = nums[left]
        while left < right:
            middle = left + ((right - left) // 2)
            
            if nums[middle] < nums[left]: #this is a true
                right = middle
            else:
                left = middle + 1
            if nums[left] < smaller:
                smaller = nums[left]
        return smaller

obj = Solution()
print(obj.findMin([3,1,2]))
