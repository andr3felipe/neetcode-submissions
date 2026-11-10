class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push either val or the current minimum into stackMin
        if not self.stackMin or val <= self.stackMin[-1]:
            self.stackMin.append(val)
        

    def pop(self) -> None:
        if self.stack:
            if self.stack.pop() == self.stackMin[-1]:
                self.stackMin.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

        

    def getMin(self) -> int:
        return self.stackMin[-1] if self.stackMin else None
        
