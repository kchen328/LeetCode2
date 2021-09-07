class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                # closing bracket
                if stack:
                    peek = stack[-1]
                    if char == ')':
                        if peek != '(':
                            return False
                        stack.pop()
                    elif char == '}':
                        if peek != '{':
                            return False
                        stack.pop()
                    elif char == ']':
                        if peek != '[':
                            return False
                        stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
