class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}

        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] = seen[c] + 1
    
        for c in t:
            if c not in seen:
                return False
            seen[c] = seen[c] - 1
            if seen[c] == 0:
                del seen[c]
            
        return len(seen) == 0
#Time complexity: O(n)
#Space complecity: O(n)