

def evalRPN(tokens):
    """
        逆波兰表达式求值
    """
    stack = []
    for item in tokens:
        if item not in {"+", "-", "*", "/"}:
            stack.append(item)
        else:
            first_num = stack.pop()
            second_num = stack.pop()
            stack.append(int(eval(f'{second_num} {item} {first_num}')))   # 第一个出来的在运算符后面
    return int(stack.pop()) # 如果一开始只有一个数，那么会是字符串形式的

aaa = evalRPN(["2","1","+","3","*"])
print(aaa)      # 9