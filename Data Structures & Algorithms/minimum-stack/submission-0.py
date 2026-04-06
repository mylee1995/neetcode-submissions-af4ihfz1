class MinStack:

    def __init__(self):
        self.all_elements = []
        self.min_elements = []

    def push(self, val: int) -> None:
        self.all_elements.append(val)
        if len(self.min_elements) == 0:
            self.min_elements.append(val)
        else:
            if val <= self.min_elements[-1]:
                self.min_elements.append(val)

    def pop(self) -> None:
        val = self.all_elements.pop()
        if val == self.min_elements[-1]:
            self.min_elements.pop()

        

    def top(self) -> int:
        return self.all_elements[-1]
        

    def getMin(self) -> int:
        return self.min_elements[-1]
        
