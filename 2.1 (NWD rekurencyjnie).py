def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)

a = int(input("podaj pierwszą liczbę"))
b = int(input("podaj drugą liczbę"))

w = nwd(a, b)

print("NWD wynosi",w)