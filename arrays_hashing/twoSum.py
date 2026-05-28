class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        needed = {}

        for i in range(len(nums)):
            if nums[i] in needed:
                return [i, needed[nums[i]]]
            else:
                remainder = target - nums[i]
                needed[remainder] = i



test = Solution()
print(test.twoSum([-3,4,3,90], 0))