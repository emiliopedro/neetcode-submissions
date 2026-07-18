class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}
        for num in nums:
            if num in occur:
                occur[num] += 1
            else:
                occur[num] = 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, fre in occur.items():
            freq[fre].append(num)
        
        final = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if len(final) == k:
                    return final