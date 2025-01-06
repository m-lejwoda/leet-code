class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        l, r = 0, len(s) - 1
        if s == "":
            return True
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True





s = Solution()
print(s.isPalindrome('aab'))
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(s.isPalindrome(s = "abba"))
print(s.isPalindrome(s = "race a car"))
print(s.isPalindrome(s = "  "))
print(s.isPalindrome(s = " apG0i4maAs::sA0m4i0Gp0"))