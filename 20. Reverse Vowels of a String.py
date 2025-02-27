class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        start, end = 0, len(s) - 1
        while end > start:
            if s[start].lower() in vowels and s[end].lower() in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            if s[start].lower() not in vowels:
                start += 1
            if s[end].lower() not in vowels:
                end -= 1

        return "".join(s)
