def tokenize(exp):
    token = []
    temp_num = ""
    operator_allowed = "/*-+%"
    for ch in exp:
        if ch == " ":
            continue

        if ch.isdigit() or ch == ".":
            temp_num += ch
        
        elif ch in operator_allowed:
            if temp_num == "" and token and token[-1] in operator_allowed:
                print("Invalid: two operators in a row")
                return None
            
            if temp_num != "":
                token.append(temp_num)

            token.append(ch)
            temp_num = ""
        
        else:
            print('invalid input')
            return None
    if temp_num != "":
        token.append(temp_num)
    return token

def evaluate(tokens):
    temp_tokens = []
    i = 0

    while i < len(tokens):
        if tokens[i] in "*/":
            operand_1 = float(temp_tokens.pop())
            operand_2 = float(tokens[i+1])

            if tokens[i] == "*":
                temp_tokens.append(operand_1 * operand_2)

            elif tokens[i] == "/":
                if operand_2 == 0 :
                    print("Cannot divide by zero")
                    return None
                temp_tokens.append(operand_1 / operand_2)
            
            elif tokens[i] == "%":
                temp_tokens.append(operand_1 % operand_2)               #  % is modulos
            
            i += 2

        else:
            temp_tokens.append(tokens[i])
            i += 1



    result = float(temp_tokens[0])
    i = 1
    while i < len(temp_tokens):
        operator = temp_tokens[i]
        operand = float(temp_tokens[i+1])

        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand

        i += 2 
    
    if result.is_integer():
        result = int(result)
    
    return result


x = str(input().strip())
tokens=tokenize(x)

if tokens is None:
    print("Fix your input")
else:
    print(tokens)
    print(evaluate(tokens))



