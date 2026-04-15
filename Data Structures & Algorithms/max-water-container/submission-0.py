class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        start = 0
        end = len(heights) - 1

        while start < end:
            vol = (end - start) * min(heights[start], heights[end])

            if vol > max:
                max = vol
            
            if heights[end] < heights[start]:
                end -= 1
            else:
                start += 1
            
        return max