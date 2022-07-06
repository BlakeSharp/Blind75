class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area = 0, len(height)-1, 0
        while(left < right):
            w = right-left
            h = min([height[left], height[right]])
            area = max([area, h*w])
            if(height[left] < height[right]):
                left += 1
            elif(height[right] < height[left]):
                right -= 1
            else:
                left += 1
                right -= 1
        return area


