class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in ransomNote:
            if dict.get(i):
                if dict[i] >= 1:
                    dict[i] -= 1
            else:
                return False
        return True

s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct(ransomNote = "aa", magazine = "aab"))