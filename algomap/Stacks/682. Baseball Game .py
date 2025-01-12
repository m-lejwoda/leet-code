from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                first, second = stack[-1], stack[-2]
                stack.append(first + second)
            elif operation == 'D':
                stack.append(2 * stack[-1])
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)





s = Solution()
print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
print(s.calPoints(["1","C"]))