from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                if len(stack) > 1:
                    stack.append(stack.pop()+stack.pop())
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first/second))
            else:
                stack.append(int(token))
        return stack[0]

s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))