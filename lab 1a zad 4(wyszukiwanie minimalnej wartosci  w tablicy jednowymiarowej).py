tablica=[8,9,17,24,-2,10,5879]
min=tablica[0]
for i in tablica:
    if min>i:
        min=i
print(f'Minimalna wartość w tablicy to {min}')