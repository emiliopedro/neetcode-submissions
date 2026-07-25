def binarysearch(arr, inf, target):
    sup = len(arr)-1

    while inf <= sup:
        mid = (inf + sup) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            inf = mid + 1
        elif arr[mid] > target:
            sup = mid - 1

    return False
    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplets = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = binarysearch(nums, j+1, -nums[i] - nums[j])
                if k and [nums[i], nums[j], nums[k]] not in triplets:
                    triplets.append([nums[i], nums[j], nums[k]])
        
        return triplets
                
                