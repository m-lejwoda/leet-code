class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        str1_length = len(str1)
        str2_length = len(str2)
        for i in range(1, str2_length + 1):
            if str2_length % i == 0 and str1_length % i == 0:
                if str1 == str2[:i] * int(str1_length / i):
                    if str2 == str2[:i] * int(str2_length / i):
                        res = str2[:i]
        return res
# from math import gcd
#
#
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1+str2!=str2+str1:
#             return ""
#         return str1[:gcd(len(str1), len(str2))]
sol = Solution()


# sol.gcdOfStrings('abc', 'abc')
print(sol.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
print("-------------------------------")
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print("-------------------------------")
print(sol.gcdOfStrings("ABCABC", "ABC"))
print("-------------------------------")
print(sol.gcdOfStrings("AAAAAAAAA", "AAACCC"))
