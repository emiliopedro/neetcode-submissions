class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = []
        for i in nums:
            if i-1 not in nums:
                curr = 1
                j = i + 1
                while j in nums:
                    curr += 1
                    j += 1
                consec.append(curr)
        if len(consec) > 0:
            return max(consec)
        else:
            return 0
