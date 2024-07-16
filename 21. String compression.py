from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0
        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            if count > 1:
                for el in str(count):
                    ans += 1
                    chars[ans] = el
            ans += 1
        return ans

sol = Solution()
sol.compress(["a","a","b","b","c","c","c"])
sol.compress(["a"])
sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])