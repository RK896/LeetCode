from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        max = 0

        while left < right:
            area = min(height[left], height[right])*(right-left)
            if area > max:
                max = area
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))