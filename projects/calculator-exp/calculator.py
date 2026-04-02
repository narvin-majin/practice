def tokenize(exp):
    token = []
    temp_num=""
    operator_allowed="/*-+"
    for ch in exp:
        if ch == " ":
            continue

        if ch.isdigit():
            temp_num += ch
        
        elif ch in operator_allowed:
            if not token and temp_num == "":
                print("Invalid: cannot start with operator")
                return None

            if token and token[-1] in operator_allowed:
                print("Invalid: two operators in a row")
                return None
            
            if temp_num != "":
                token.append(temp_num)

            token.append(ch)
            temp_num=""
        
        else:
            print('invalid input')
            return None
    if temp_num != "":
        token.append(temp_num)
    return token

def evaluate(tokens):
    a = int(tokens[0])
    op = tokens[1]
    b = int(tokens[2])

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/" and b == 0:
        print("cannot divide by zero")
        return None
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b

x = str(input().strip())
tokens=tokenize(x)
print(tokens)
print(evaluate(tokens))



