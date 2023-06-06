def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
           stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Nieprawidłowe wyrażenie")
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2
            else:
                raise ValueError("Nieznany operator: " + token)
            stack.append(result)
    if len(stack) != 1:
        raise ValueError("Nieprawidłowe wyrażenie")

    return stack[0]

expression = input("Podaj wyrażenie  w notacji postfiksowej: ").split()
result = evaluate_postfix(expression)
print("Wynik to ", result)