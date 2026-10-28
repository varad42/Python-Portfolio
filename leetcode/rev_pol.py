# number → push; operator → pop right, pop left, push left ⊕ right”, Time O(n), Space O(n)

def evalRPN(tokens):

    stack = []
    for i in tokens:
        if i == "+":
            right_int = stack.pop()
            left_int = stack.pop()
            val = left_int + right_int
            stack.append(val)
        elif i == "-":
            right_int = stack.pop()
            left_int = stack.pop()
            val = left_int - right_int
            stack.append(val)
        elif i == "*":
            right_int = stack.pop()
            left_int = stack.pop()
            val = left_int * right_int
            stack.append(val)
        elif i == "/":
            right_int = stack.pop()
            left_int = stack.pop()
            val = int(left_int / right_int)
            stack.append(val)
        else:
            stack.append(int(i))

    return stack[-1]


print(evalRPN(["2","1","+","3","*"]))       # 9
print(evalRPN(["4","13","5","/","+"]))      # 6
print(evalRPN(["5","3","-"]))               # 2
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22