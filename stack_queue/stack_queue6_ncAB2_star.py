

def IsPopOrder(pushV, popV):
    """
        栈的压入弹出
    """
    n = len(pushV)
    stack = []
    j = 0
    for i in range(n):
        while j < n and (len(stack) == 0 or stack[-1] != popV[i]):
            stack.append(pushV[j])
            j += 1
        if stack[-1] == popV[i]:
            stack.pop()
        else:
            return False
    return True

aaa = IsPopOrder([1,2,3,4,5],[4,5,3,2,1])
bbb = IsPopOrder([1,2,3,4,5],[4,3,5,1,2])
print(aaa)
print(bbb)