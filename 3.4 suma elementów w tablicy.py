def suma_tablicy(tablica, a, b):
    if a == b:
        return tablica[a]
    c = (a + b) // 2
    suma_a = suma_tablicy(tablica, a, c)
    suma_b = suma_tablicy(tablica, c + 1, b)
    return suma_a + suma_b
tablica = [4, 9, 2, 7, 19, 1, 8, 3, 6]
suma_elementow = suma_tablicy(tablica, 0, len(tablica) - 1)
print("Suma elementów to :", suma_elementow)