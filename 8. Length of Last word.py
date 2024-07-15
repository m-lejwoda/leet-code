class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(s.split()[-1])
        #return 'The last word is "{}" with length {}.'.format(arr[-1], len(arr[-1]))

s = Solution()
print(s.lengthOfLastWord('Hello World'))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))