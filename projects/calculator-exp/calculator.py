def tokenize(expression):
    if expression == None:
        return None
    else:
        token = []
        current_number = ""
        operator_allowed = "/*-+%"
        for ch in expression:
            if ch == " ":
                continue
            
            
            if ch.isdigit() or ch == ".":
                current_number += ch
            
            elif ch in operator_allowed:
                if current_number == "" and token and token[-1] in operator_allowed:
                    print("Invalid: two operators in a row")
                    return None
                
                if current_number != "":
                    token.append(current_number)

                token.append(ch)
                current_number = ""
            
            else:
                print('invalid input')
                return None
        if current_number != "":
            token.append(current_number)
        return token

def evaluate(tokens):
    if tokens == None:
        return None
    else:
        temporary_token = []
        i = 0

        while i < len(tokens):
            if tokens[i] in "*/%":
                operand_1 = float(temporary_token.pop())
                operand_2 = float(tokens[i+1])

                if tokens[i] == "*":
                    temporary_token.append(operand_1 * operand_2)

                elif tokens[i] == "/":
                    if operand_2 == 0 :
                        print("Cannot divide by zero")
                        return None
                    temporary_token.append(operand_1 / operand_2)
                
                elif tokens[i] == "%":
                    temporary_token.append(operand_1 % operand_2)               #  % is modulos
                
                i += 2

            else:
                temporary_token.append(tokens[i])
                i += 1



        result = float(temporary_token[0])
        i = 1
        while i < len(temporary_token):
            operator = temporary_token[i]
            operand = float(temporary_token[i+1])

            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand

            i += 2 
        
        if result.is_integer():
            result = int(result)
        
        return result

def para_exp(expression):
    if expression is None:
        return None
    
    # validate parentheses structure
    balance = 0
    for ch in expression:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
            if balance < 0:
                print("Invalid parentheses order")
                return None

    if balance != 0:
        print("Missing parentheses")
        return None
    
    
    
    while "(" in expression:
        start = expression.rfind("(")
        end = expression.find(")", start)
        inner = expression[start+1:end]
        value = str(evaluate(tokenize(inner)))
        if value is None:
            return None
        expression = expression[:start] + value + expression[end + 1 :]
        
    else:
        return expression

def _input():
    while True:
        expression = input("Enter expression (or 'exit'): ")

        if expression.lower() == "exit":
            break

        result = evaluate(tokenize(para_exp(expression)))

        if result is not None:
            print("Result:", result)

_input()


