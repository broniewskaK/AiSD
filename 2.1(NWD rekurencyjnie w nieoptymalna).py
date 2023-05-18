def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
a = int(input("podaj pierwszą liczbe: "))
b = int(input("podaj drugą liczbe: "))

w=NWD(a,b)
print("NWD wynosi",w)