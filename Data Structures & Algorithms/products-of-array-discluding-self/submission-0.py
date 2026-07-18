class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        has_zero = False
        result = [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] == 0 and has_zero:
                return result
            if nums[i] == 0:
                has_zero = True
                zero_idx = i
            else:
                prod *= nums[i]

        if has_zero:
            result[zero_idx] = prod
            return result
        else:
            for i in range(len(nums)):
                result[i] = prod//nums[i]
            return result