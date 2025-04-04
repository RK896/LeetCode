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
    
    def topKFrequent_bucket_sort(self, nums: List[int], k:int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums)+1)]

        for x in nums: 
            count[x] = count.get(x,0) + 1
        
        for num, counts in count.items():
            buckets[counts].append(num)
        
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result




sol = Solution()
print(sol.topKFrequent_bucket_sort([1,1,1,2,2,3], 2))
print(sol.topKFrequent_bucket_sort([1], 1))
