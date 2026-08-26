class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        #note that this approach of moving to the left or the right in the array only works because the array is sorted
        #we are skipping combinations by adding the smallest available with the largest available if the sum is too much or too little we skip parts based on the big or small indices
        while left < right: #O(n/2) 
            result = numbers[left] + numbers[right] 
            
            if result == target:
                return [left + 1, right + 1]
            
            #if too big, decrease
            if numbers[left] + numbers[right] > target:
                right -= 1
            
            #if too small increase
            if numbers[left] + numbers[right] < target: 
                left += 1
        return []

#time complexity: O(n)
#space complexity: O(1)