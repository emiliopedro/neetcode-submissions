class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n-2,-1,-1):
            j = i+1
            while (temperatures[j]<=temperatures[i]) and (j<n):
                if res[j] == 0:
                    j = i
                    break
                j += res[j]
            if j<n:
                res[i] = j-i
        return res