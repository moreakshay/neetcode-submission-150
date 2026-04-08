class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []    
    
    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            cur_min = min(self.min_stack[-1], val)
            self.min_stack.append(cur_min)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.min_stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

        
