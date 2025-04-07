from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1

            while left < right: 
                sum = a + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([a,nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
