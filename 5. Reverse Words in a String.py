class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        result_arr = []
        for i in s[::-1]:
            if len(i.strip()) == 0:
                continue
            else:
                result_arr.append(i)
        result = ' '.join(result_arr)
        return result



sol = Solution()
print(sol.reverseWords("Hello World!"))
print(sol.reverseWords("a good   example"))
print(sol.reverseWords(" hello world"))