class MyQueue:

    def __init__(self):
        self.array=[]
        self.index=0
    def push(self, x: int) -> None:
        self.array.append(x)
        self.index +=1
    def pop(self) -> int:
        self.index -=1
        return self.array.pop(0)

    def peek(self) -> int:
        return self.array[0]

    def empty(self) -> bool:
        if(self.index==0):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()