class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numKeys = {}
        for n in nums:
            if n not in numKeys:
                numKeys[n] = True
            else:
                return True
        return False
        
