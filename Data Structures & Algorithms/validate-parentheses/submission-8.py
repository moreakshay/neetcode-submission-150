class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        stack = []
        bracket_map = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        for c in s:
            #opening bracket
            if c in bracket_map:
                stack.append(c)
            else:
                #empty stack
                if not stack:
                    return False
                top = stack.pop()
                #invalid if not the same closing bracket
                if bracket_map[top] != c:
                    return False
        
        return not stack
        