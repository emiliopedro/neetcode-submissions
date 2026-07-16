class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i in range(len(nums)):
            dup.add(nums[i])
            if len(dup) != (i+1):
                return True
        return False
