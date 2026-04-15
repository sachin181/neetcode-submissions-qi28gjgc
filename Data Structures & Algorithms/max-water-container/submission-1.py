class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        start = 0
        end = len(heights) - 1

        while start < end:
            max_vol = max(max_vol, (end - start) * min(heights[start], heights[end]))
            
            if heights[end] < heights[start]:
                end -= 1
            else:
                start += 1
            
        return max_vol