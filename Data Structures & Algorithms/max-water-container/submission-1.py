class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            formula = min(heights[left],heights[right]) * (right-left)
            if heights[right] >= heights[left]:
                left += 1
                if formula > largestArea:
                    largestArea = formula
            elif heights[right] < heights[left]:
                right -= 1
                if formula > largestArea:
                    largestArea = formula
        return largestArea