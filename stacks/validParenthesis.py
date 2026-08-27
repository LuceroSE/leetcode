class Solution:
    def isValid(self, s: str) -> bool:
        #valid brackets
        brackets = {"(":")",
                    "[":"]",
                    "{":"}"}
        #stack to store closing braces
        stack = Stack()
        
        for c in s:
            #if c is a opening bracket, store its corresponding closing bracket in the stack
            if c in brackets:
                stack.push(c) #save opening bracket
            else: #c is a closing bracket
                if stack.top():
                    latestOpen = stack.top() #get the most recent open bracket 
                    if c == brackets[latestOpen]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        #is stack is empty then all corresponding opening brackets had their closing brackets at the right order (this works because of how the stack is structured)
        if stack.isEmpty():
            return True
        return False

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return self.stack
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return self.stack
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return "{}".format(self.stack)




obj = Solution()
print(obj.isValid("]"))