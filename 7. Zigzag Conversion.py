class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for r in range(numRows):
            print("r")
            print(r)
            increment = 2 * (numRows - 1)
            # To dziala dla pierwszego i ostatniego
            for i in range(r, len(s), increment):
                print(i)
                res += s[i]
                # to dla reszty
                if (r>0 and r<numRows-1 and i + increment - 2 * r < len(s)):
                    print("i + increment - 2")
                    print(i + increment - 2)
                    res += s[i + increment - 2 * r]
        return res

sol = Solution()
sol.convert("PAYPALISHIRING", 3)