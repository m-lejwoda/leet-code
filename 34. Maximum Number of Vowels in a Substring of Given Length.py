class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_number = 0
        actual_number = 0
        vowel_letters = ['a', 'e', 'i', 'o','u']
        i,j = 1, k
        for z in range(k):
            if s[z] in vowel_letters:
                max_number += 1
                actual_number += 1
        while j<len(s):
            if s[i - 1] in vowel_letters:
                actual_number -= 1
            if s[j] in vowel_letters:
                actual_number += 1
            max_number = max(actual_number, max_number)
            i += 1
            j += 1
        return max_number