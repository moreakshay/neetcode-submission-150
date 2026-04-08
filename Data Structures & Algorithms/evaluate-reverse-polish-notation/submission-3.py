class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        for token in tokens:
            if token == "+":
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif token == "-":
                b = stack.pop()
                total = stack.pop() - b
                stack.append(total)
            elif token == "*":
                total = stack.pop() * stack.pop()
                stack.append(total)
            elif token == "/":
                b = stack.pop()
                total = stack.pop() / b
                stack.append(int(total))
            else:
                stack.append(int(token))
        return stack.pop()