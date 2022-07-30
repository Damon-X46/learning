"""
    栈
"""
class stack_implement:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.stack == []:
            print('error')
            return
        ans = self.stack.pop()
        print(ans)
    def top(self):
        if self.stack == []:
            print('error')
            return
        print(self.stack[-1])

def main():
    s = stack_implement()
    input_num = int(input())
    for i in range(input_num):
        a = input().strip().split(' ')
        if a[0] == 'push':
            s.push(int(a[1]))
        elif a[0] == 'pop':
            s.pop()
        elif a[0] == 'top':
            s.top()
        
if __name__ == '__main__':
    main()