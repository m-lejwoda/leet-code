class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_symbols[s[i]] < roman_symbols[s[i + 1]]:
                res -= roman_symbols[s[i]]
            else:
                res += roman_symbols[s[i]]
        return res







s = Solution()
# print(s.romanToInt("III"))
# print(s.romanToInt("XVIII"))
print(s.romanToInt("LVIII"))
# print(s.romanToInt("LIV"))
# print(s.romanToInt("MCMXXCV"))
#1985