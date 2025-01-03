from math import ceil


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = float('inf')
        dict_text = {}
        ballons = ['b','a','l','o','n']
        for i in text:
            if i in ballons:
                if i in dict_text:
                    dict_text[i] += 1
                else:
                    dict_text[i] = 1
        for b in ballons:
            if b in dict_text:
                if b == "l" or b == "o":
                    res = min(res, int(dict_text[b]/2))
                else:
                    res = min(res, dict_text[b])
                dict_text[b] -= 1
            else:
                return 0
        return 0 if res == float('inf') else res


s = Solution()
print(s.maxNumberOfBalloons(text = "nlaebolko"))
print(s.maxNumberOfBalloons(text = "loonbalxballpoon"))
print(s.maxNumberOfBalloons(text = "leetcode"))
print(s.maxNumberOfBalloons(text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
