class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        app = {}
        for i in nums:
            if i in app:
                return True
            else:
                app[i] = 1
        return False