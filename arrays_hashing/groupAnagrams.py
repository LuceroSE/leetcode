class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        general = {} #dict mapping repeated alphabetic characters to the number of times they appear

        for word in strs:  #O(n) where n is the number of words in the list
            wordCount = [0] * 26 
            for c in word:   #O(m) where m is the number of characters in each word
                wordCount[ord(c) - ord("a")] = wordCount[ord(c) - ord("a")] + 1  #mapping letter to the position in the list with ascii values
            generalKey = tuple(wordCount)  #turning list into a immutable type for a hashable key.  O(27) time complexity
            if generalKey not in general:
                general[generalKey] = [word]
            else:
                general[generalKey].append(word)
        
        return list(general.values())

#Time complexity: O(n * m + 26) meaning O(n * m)
#Space complexity: O(n)
