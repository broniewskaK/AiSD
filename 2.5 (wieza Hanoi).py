def hanoi(n,A,B,C):
    if n > 0:
        hanoi(n-1,A,C,B)
        print(f"Przenies dysk {n} z {A} na {C}")
        hanoi(n-1,C,B,A)
    elif n<=0:
        return print('niepoprawna liczba klocków')
n=int(input('podaj liczbę krążków'))
hanoi(n, "A", "B", "C")