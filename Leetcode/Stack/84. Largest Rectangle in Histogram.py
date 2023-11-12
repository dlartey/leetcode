class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i,h in enumerate(heights):
            current = i 
            while (stack and stack[-1][1] > h):
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                current = index
            stack.append((current,h))
        
        for i,h in stack:
            maxArea = max(maxArea,h* (len(heights)-i))
        
        return maxArea