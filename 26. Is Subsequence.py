class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if len(s) > len(t):
            return False
        i,j = 0, 0
        count = 0
        while i< len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                count += 1
                if count == len(s):
                    return True
            else:
                j += 1
        return False

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '': return True
        p1 = 0
        for char in t:
            # check if the current letter in s is found
            if s[p1] == char:
                p1 += 1
                # if it is the last letter in s we are looking for then it is subsequence
                if p1 == len(s):
                    return True
        return False
