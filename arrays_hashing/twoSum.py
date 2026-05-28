class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        needed = {}

        for i in range(len(nums)):
            if nums[i] in needed:
                return [i, needed[nums[i]]]
            else:
                remainder = target - nums[i]
                needed[remainder] = i
# Time complexity: linear

