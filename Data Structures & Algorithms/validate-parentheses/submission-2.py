class Solution:
    def isValid(self, s: str) -> bool:
        corr = {'[': ']', '{': '}', '(': ')'}
        
        stack = []
        for i in s:
            if i in corr:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if corr[stack[-1]] != i:
                    return False
                else:
                    stack.pop(-1)
            
        if len(stack) == 0:
            return True
        return False