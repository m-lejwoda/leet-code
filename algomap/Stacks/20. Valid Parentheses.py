class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
                continue
            if bracket == ")" or bracket == "]" or bracket == "}":
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp == "(":
                    if bracket != ")":
                        return False
                if temp == "[":
                    if bracket != "]":
                        return False
                if temp == "{":
                    if bracket != "}":
                        return False
        if len(stack) > 0:
            return False
        return True

s = Solution()
print(s.isValid("("))
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))