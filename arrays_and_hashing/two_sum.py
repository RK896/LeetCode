from typing import List
class Solution:
    def twoSum_two_pointers(nums, target):
        left = 0
        right = len(nums)-1

        indexed_list = []

        for i,num in enumerate(nums):
            indexed_list.append((num, i))
        indexed_list.sort()

        while left < right:
            sum = indexed_list[left][0] + indexed_list[right][0]

            if sum == target:
                return [indexed_list[left][1], indexed_list[right][1]]
            if sum < target:
                left+=1
            elif sum > target:
                right-=1
        
        return [0,0]
    

    # def twoSum_hash_map (self, nums:List[int], target: int) -> List[int]:


sol = Solution()
print(sol.twoSum_two_pointers([2,7,11,15], 9))
