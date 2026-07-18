class Solution:
    def isPalindrome(self, s: str) -> bool:
        phr = s.casefold()

        new_phr = []
        for l in phr:
            if l.isalnum():
                new_phr.append(l)
        new_phr = ''.join(new_phr)
        
        for i in range(len(new_phr) // 2):
            if new_phr[i] != new_phr[-i-1]:
                return False
        return True