class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        biggest = 0
        while (left < right):
            area = (right - left) * (min(heights[left],heights[right]))
            if biggest < area:
                biggest = area
            if (left < right and heights[left] <= heights[right]):
                left += 1
            elif (left < right and heights[left] > heights[right]):
                right -= 1
        return biggest

        