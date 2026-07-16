class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur = {}
        for i in s:
            if i in occur:
                occur[i] += 1
            else:
                occur[i] = 1

        for i in t:
            if i not in occur:
                return False
            else:
                occur[i] -= 1
                if occur[i] < 0:
                    return False
        
        for k in occur:
            if occur[k] > 0:
                return False
        
        return True