class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        additions = []
        nums.sort() #sorts in place
        i = 0
        while i < len(nums): #O(n)
            #if we are dealing with repeated numbers [1,1,1,2,3,4,4] we skip all the next repeated values of i
            #this only works because the list is sorted, otherwise the numbers would be scatered all over the place
            #[1,3,4,1,2,4,1,1]
            if i != 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            
            #now we apply the 2Sum II algorithm in the remaining of the list finding 2 numbers that add to i and make 0
            left = i + 1
            right = len(nums) - 1
            while left < right: #O(n) 
                result = nums[i] + nums[left] + nums[right]

                if result > 0:
                    #if result is > 0 try with a smaller number
                    right -= 1
                elif result < 0:
                    #if result < 0 try with a bigger number
                    left += 1
                else:
                    #if result = 0 add the numbers to our result list
                    additions.append([nums[i], nums[left], nums[right]])
                    #now moving our left pointer (we could also move the right but moving repeated left pointer values already garantees a different combination of numbers to add)
                    left += 1
                    #making sure we do skip repeated numbers in the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
        return additions


#Time complexity: O(n log n)+O (n*n) = O(n^2) 
#Space complexity: O(1) even though some sorting algorithms might take extra space

##IMPORTANT: Sorting isn't only helping the two-pointer search, it's also ensuring 
#that the same three values can't appear in different permutations in the output. 
"""Because after sorting, the values are always in increasing order:
[1, 2, 4]

And the pointers always satisfy:

i < left < right

Therefore they can only select:

nums[i] <= nums[left] <= nums[right]

   1          2            4

They can never select:

[2, 1, 4]

because once i points to 2, left must be to the right of 2, and since the array is sorted therefore cannot point back to 1.

So sorting + always moving left-to-right guarantees every triplet is generated in one consistent order (like in addition in TwoSum II):

[1, 2, 4]  ✅
[2, 1, 4]  ❌
[4, 1, 2]  ❌

That's why different permutations of the same three numbers can't appear in the result.
"""


obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))