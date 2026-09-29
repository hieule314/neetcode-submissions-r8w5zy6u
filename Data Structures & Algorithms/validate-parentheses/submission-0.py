class Solution:
    def isValid(self, s: str) -> bool:
        # Understand: Given a string s, output boolean T/F if 
        # every open bracket is closed by the same type of close 
        # bracket

        # Stack: LIFO (last in first out)

        # Plan: Mapping (dictionary)
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack: # if len(stack) == 0
            return True
        return not stack
                