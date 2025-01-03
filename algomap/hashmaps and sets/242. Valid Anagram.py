class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_set = dict()
        if len(s) != len(t):
            return False
        for i in t:
            if i in dict_set:
                dict_set[i] += 1
            else:
                dict_set[i] = 1
        for i in s:
            if dict_set.get(i):
                if dict_set[i] >= 1:
                    dict_set[i] -= 1
                else:
                    return False
            else:
                return False
        return True

s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))
print(s.isAnagram(s = "rat", t = "car"))