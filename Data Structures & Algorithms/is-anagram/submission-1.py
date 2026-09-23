class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        let = {}

        for l in s:
            if l in let:
                let[l] += 1
            else:
                let[l] = 1
        
        for l in t:
            if l not in let:
                return False
            let[l] -= 1
            if let[l] < 0:
                return False
        
        for l in let:
            if let[l] != 0:
                return False
        
        return True