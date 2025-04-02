from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        for x in strs:
            alphabet = [0]*26
            for char in x:
                alphabet[ord(char)-ord('a')] += 1
            key = tuple(alphabet)
            result[key].append(x)
        
        return list(result.values())
        
sol = Solution()
print (sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))