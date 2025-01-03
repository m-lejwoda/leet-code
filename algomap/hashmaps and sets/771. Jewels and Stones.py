class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        res = 0
        for i in stones:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        set_jewels = set(jewels)
        for i in set_jewels:
            if i in dict:
                res += dict[i]
        return res

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
print(s.numJewelsInStones("z", "Z"))
