class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1 
        leftMax = height[left]
        rightMax = height[right]
        water = 0
        while left < right:
            if leftMax < rightMax:
                left +=1
                if leftMax < height[left]:
                    leftMax = height[left]
                water += leftMax - height[left]
            else:
                right -= 1
                if rightMax < height[right]:
                    rightMax = height[right] 
                water += rightMax - height[right]
        return water
            



obj = Solution()
print(obj.trap([0,2,0,3,1,0,1,3,2,1]))