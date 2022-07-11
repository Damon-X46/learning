

class MinStack:
    """
        剑指offer30
        定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
    """
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float('inf')]     # 辅助栈，存最小值的

    def push(self, x: int):
        self.stack.append(x)
        self.min_stack.append(min(self.min_stack[-1], x))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        pass

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.min()
obj.pop()
param_2 = obj.top()
param_3 = obj.min()
pass