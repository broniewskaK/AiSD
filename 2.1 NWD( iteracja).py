def nwd():
    a=int(input('podaj pierwszą liczbę'))
    b=int(input('podaj drugą liczbę'))
    if a==b:
        return a
    else:
        while b != 0:
            c = a % b
            a = b
            b = c
        return a
print("NWD to",nwd())