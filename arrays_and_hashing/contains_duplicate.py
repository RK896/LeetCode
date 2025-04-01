from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))
    print(solution.containsDuplicate([4, 2, 3, 1]))
