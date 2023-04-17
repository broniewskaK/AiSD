n=int(input('podaj liczbę wyrazów ciągu'))
s=0
while n<=0:
    n=int(input('liczba wyrazów ciągu musi być dodatnia, podaj n'))
else:
    for i in range(n):
        a=int(input('Podaj liczbę'))
        if a<0:
            s+=1
    print(F'liczba wyrazów mniejszych od zero to {s}')
