class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len (s):
            return False
        my_list = [0]*26

        for i in range(len(s)):
            my_list[ord(s[i])-ord('a')]+=1
            my_list[ord(t[i])-ord('a')]-=1
            
        
        return my_list == ([0]*26)

sol = Solution()
print(sol.isAnagram("tacocat", "catotac"))
print(sol.isAnagram("car", "rat"))