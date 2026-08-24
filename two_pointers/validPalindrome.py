class Solution:
    def isPalindrome(self, s: str) -> bool:

        end = len(s) - 1
        beginning = 0

        while beginning < end:
            while beginning < end and not self.isAlphaNum(s[beginning]):
                beginning += 1
            while end > beginning and not self.isAlphaNum(s[end]):
                end -= 1
            if s[beginning].lower() != s[end].lower():  #.lower() is O(n) since we are just calling it in only one character and not a string
                return False
            beginning += 1
            end -= 1
        return True
    
    def isAlphaNum(self, c):
        if "Z" >= c >= "A" or "z" >= c >= "a" or "9" >= c >= "0":
            return True
        return False
    

#Time Complexity: O(n)
#Space complexity: O(1) since we did not create extra data structures