class Solution:
    def isValid(self, s: str) -> bool:
        inpToOutMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for char in s:
            if char not in inpToOutMap:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif inpToOutMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False