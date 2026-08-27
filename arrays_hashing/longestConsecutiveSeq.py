class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) #turning into set to get O(1) membership checks
        longestSeq = 0      #starting to count from 0 to find the longest conseq sequence 
        for n in numsSet:      
            #pay attention that we do not skip any min value in the sequence like we did in 1st solution since we are not using
            #indices, we are checking membership, always checking if we are at the min, if we are at the min then the rest of the if body happens
            if (n - 1) not in numsSet: #if we are at the very min number (start of the sequence), if not skip
                length = 0            #lets start the count of the length of this specific sequence
                while (n + length) in numsSet: #while the next number of our sequence with n is in the set 
                    length += 1                #keep looking for the end of the sequence
                if length > longestSeq:        #if the length of this sequence is greater than previous sequences in the list
                    longestSeq = length        #update the longest sequence count
        return longestSeq 