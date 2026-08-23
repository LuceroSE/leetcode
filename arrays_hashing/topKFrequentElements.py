class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [0] * (len(nums) + 1) 
        # for inputs with just one 1 value in the list (otherwise [0] * 1 = [0] and the 1 index apperance for the number will be out of range)
        for n in nums:  # going through each number in the list O(n)  
            if n not in count:
                count[n] = 0
            count[n] += 1
        #the length of the dictionary is <= to the length of the list of numbers O(n)
        for (key,v) in count.items():
            if frequency[v] == 0:   
                frequency[v] = []
            frequency[v].append(key)

        #turining result [[2], [3]] into [2,3]
        result = []
        for sublist in frequency: #for sublist in frequency is O(n), since there can be at max n + 1 indices in frequency
            if sublist != 0:
                for num in sublist: 
                    ##for num in sublit is O(n) since there can be at max n items in (ONE SINGLE) index of frequency i.e. [1,2,3,4] the frequency [0,[1,2,3,4],0,0] (each item appears only once so all added to index 1), this is NOT that for each item in the outer loop we do O(n) in the inner loop, we do less than that. So it is not quadratic       
                    result.append(num) 
                    """
                        [
                            [],
                            [1, 2, 3, 4],
                            [],
                            [5, 6],
                            [7]
                        ]
                        bucket 0 → 0
                        bucket 1 → 4
                        bucket 2 → 0
                        bucket 3 → 2
                        bucket 4 → 1

                        TOTAL → 7 loops in inner loop
                       scan buckets (outer loop of list frequency len n + 1 is O(n)) + scan elements of bucket (inner loop where in one particular bucket there can be 0(n) elements) 
                           O(n)                                                      +        O(n) = O(n)"""
        return result 
        
        
        
        #total time complexity O(1)

#Time complexity: O(n)
#Space complexity: O(n)