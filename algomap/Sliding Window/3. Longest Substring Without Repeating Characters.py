class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        set_arr = set()
        n = len(s)
        for r in range(n):
            while s[r] in set_arr:
                set_arr.remove(s[l])
                l+=1
            w = (r-l) + 1
            longest = max(longest, w)
            set_arr.add(s[r])
        return longest