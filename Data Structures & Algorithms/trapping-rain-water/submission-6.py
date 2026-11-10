class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxValue = 0
        res = 0

        for i in range(len(height)):
            maxLeft[i] = maxValue
            maxValue = max(maxValue, height[i])
            
        maxValue = 0
        for i in range(len(height) -1, -1, -1):
            maxRight[i] = maxValue
            maxValue = max(maxValue, height[i])
        
        for i, n in enumerate(height):
            top = min(maxLeft[i], maxRight[i])
            fill = top - n

            if fill > 0:
                res += fill

        
        return res

