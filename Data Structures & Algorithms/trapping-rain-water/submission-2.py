class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        r_max = 0
        for i in range(1, len(height)):
            if height[i-1] > r_max:
                r_max = height[i-1]
            prefix.append(r_max)

        suffix = [0]
        l_max = 0
        for i in range(len(height)-2, -1, -1):
            if height[i+1] > l_max:
                l_max = height[i+1]
            suffix.append(l_max)

        total = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[-i-1]) - height[i]
            if water > 0:
                total += water
        
        return total
