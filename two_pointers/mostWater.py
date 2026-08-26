class Solution:
    def maxArea(self, height: List[int]) -> int:
        #determining base of container
        left = 0
        right = len(height) - 1
        mostArea = 0
        while left < right:
            
            base = right - left

            if height[left] < height[right]:
                minHeight = height[left]
                left += 1

            elif height[right] < height[left]:
                minHeight = height[right]
                right -= 1
            else:# if both heights are the same 
                 # choose any of them to be the nim and calculate the area 
                 # move any of them so we can keep comparing
                minHeight = height[right]
                left += 1

            currentArea = base * minHeight 

            if mostArea < currentArea:
                mostArea = currentArea

        return mostArea

#Time complexity: O(n)
#Space complexity: O(1)