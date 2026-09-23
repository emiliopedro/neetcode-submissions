class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum():
                l += 1
                if l >= len(s):
                    break
            
            while not s[r].isalnum():
                r -= 1
                if r < 0:
                    break

            if l >= len(s) or r < 0:
                break

            if s[l].casefold() != s[r].casefold():
                return False

            l += 1
            r -= 1
        
        return True
            
