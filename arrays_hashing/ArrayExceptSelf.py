class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        #calculating prefix
        pre = 1
        i = 0
        while i < len(nums):
            result[i] = pre
            pre = nums[i] * pre
            i = i + 1
        #calculating postfix
        post = 1
        i = len(nums) - 1
        while i >= 0:
            result[i] = result[i] * post
            post = post * nums[i]
            i = i - 1
        return result
#time complexity O(n)
#space complexity O(1) since we are only creating one output array
