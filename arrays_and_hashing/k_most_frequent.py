from typing import List

class Solution:
    def topKFrequent_brute_force(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums: 
            count[x] = count.get(x,0)+1
        
        arr = []
        for num,count in count.items():
            arr.append([count, num])
        arr.sort()

        output = []
        for n in range(k):
            output.append(arr[len(arr)-n-1][1])
        return output

sol = Solution()
print(sol.topKFrequent_brute_force([1,1,1,2,2,3], 2))
print(sol.topKFrequent_brute_force([1], 1))
