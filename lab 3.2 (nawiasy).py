from STOS import Stack


def parChecker(symbolString):
    s = Stack()
    index = 0
    error = True
    while index < len(symbolString) and error:
        symbol = symbolString[index]
        if symbol == "(": s.push(symbol)
        else:
            if s.isEmpty(): error=False
            else: s.pop()
        index = index+1
    if error and s.isEmpty(): return True
    else: return False


print(parChecker('((()))'))
print(parChecker('((())))))'))
print(parChecker('(((()()(())))'))