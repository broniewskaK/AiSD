def dwumian(n, k):

    tablica = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                tablica[i][j] = 1
            else:
                tablica[i][j] = tablica[i - 1][j - 1] + tablica[i - 1][j]

    return tablica[n][k]
n = 5
k = 2
wynik = dwumian(n, k)
print("Współczynnik dwumianowy wynosi:", wynik)