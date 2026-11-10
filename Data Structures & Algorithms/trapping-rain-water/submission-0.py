class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        maxValue = 0
        res = 0

        for i in range(len(height)):
            maxLeft.append(maxValue)
            maxValue = max(maxValue, height[i])
            
        maxValue = 0
        for i in range(len(height) -1, -1, -1):
            maxRight.insert(0, maxValue)
            maxValue = max(maxValue, height[i])
        
        for i, n in enumerate(height):
            top = min(maxLeft[i], maxRight[i])
            fill = top - n

            if fill > 0:
                res += fill

        
        return res

