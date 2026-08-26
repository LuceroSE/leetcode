class Solution:
    def isPalindrome(self, s: str) -> bool:

        end = len(s) - 1
        beginning = 0

        while beginning < end:
            while beginning < end and not self.isAlphaNum(s[beginning]):
                beginning += 1
            while end > beginning and not self.isAlphaNum(s[end]):
                end -= 1
            if s[beginning].lower() != s[end].lower():  #.lower() is O(1) since we are just calling it in only one character and not a string
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

# Time Complexity: O(n)
#
# Even though there are nested while loops, this is NOT O(n^2).
# Nested loops only result in O(n^2) when the inner loop can do O(n)
# work for EACH iteration of the outer loop.
#
# Here, `beginning` only moves to the right and `end` only moves to
# the left. Neither pointer ever resets to its original position.
# Therefore, across the ENTIRE algorithm, `beginning` can move at
# most n positions and `end` can move at most n positions.
#
# The 1st inner loop may individually take O(n) in the worst case, but
# if an inner loop does a lot of work, it moves a pointer significantly
# closer to the other pointer. This means the outer loop has fewer
# iterations left to perform. The inner-loop work and outer-loop work
# are therefore not independent, so we cannot multiply them as
# O(n) * O(n).
#
# For example, if the string contains only non-alphanumeric characters,
# the first inner loop can move `beginning` almost all the way to `end`
# during the FIRST outer-loop iteration. Once beginning == end, the
# second inner loop does no work and the outer loop terminates (since their conditions are not satisfied anymore). So in
# that case we have roughly 1 outer iteration + n pointer movements,
# which is O(n), not O(n^2).
#
# On the other hand, if every character is alphanumeric, the inner
# loops do no work. The outer loop moves both pointers toward each
# other and therefore runs about n/2 times, which is also O(n).
#
# In general, regardless of how the work is distributed between the
# outer and inner loops, the two pointers can only traverse the string
# once. Thus the total amount of work grows linearly with the length
# of the string.
#
# Time:  O(n)
# Space: O(1)