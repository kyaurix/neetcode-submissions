class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                if min(heights[i], heights[j]) * (j-i) > largestArea:
                    largestArea = (min(heights[i], heights[j]) * (j-i))
        return largestArea