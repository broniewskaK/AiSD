def oblicz(n):
    if n==0 or n==1:
        return 1
    elif n>0:
        return 2*oblicz(n-1)-oblicz(n-2)

print(oblicz(2))
print(oblicz(5))