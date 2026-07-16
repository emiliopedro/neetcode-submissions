class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, val in enumerate(nums):
            if val not in comp:
                comp[target - val] = i
            else:
                return [comp[val], i]