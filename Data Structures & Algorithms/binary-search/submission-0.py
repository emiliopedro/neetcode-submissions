class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inf, sup = 0, len(nums) - 1

        while inf <= sup:
            mid = (inf + sup) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                inf = mid + 1
            elif nums[mid] > target:
                sup = mid - 1
        
        return -1