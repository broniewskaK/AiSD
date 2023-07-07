def graf():
    rodzaj_grafu = input("Jaki graf chcesz zbudować? (skierowany/nieskierowany): ")
    ilosc_wierzcholkow = int(input("Podaj ilość wierzchołków: "))

    macierz_sasiedztwa = [[0] * ilosc_wierzcholkow for _ in range(ilosc_wierzcholkow)]

    for i in range(ilosc_wierzcholkow):
        for j in range(ilosc_wierzcholkow):
            if i != j:
                polaczenie = input(f"Czy istnieje połączenie między wierzchołkiem {i} a {j}? (tak/nie): ")
                if polaczenie == 'tak':
                    macierz_sasiedztwa[i][j] = 1

    print("\nMacierz sąsiedztwa:")
    for row in macierz_sasiedztwa:
        print(row)

    lista_sasiedztwa = [[] for _ in range(ilosc_wierzcholkow)]
    for i in range(ilosc_wierzcholkow):
        for j in range(ilosc_wierzcholkow):
            if macierz_sasiedztwa[i][j] == 1:
                lista_sasiedztwa[i].append(j)

    print("\nLista sąsiedztwa:")
    for i, sasiedzi in enumerate(lista_sasiedztwa):
        print(f"{i}: {sasiedzi}")

    interpretacja_graficzna = [[' ' for _ in range(ilosc_wierzcholkow)] for _ in range(ilosc_wierzcholkow)]
    for i in range(ilosc_wierzcholkow):
        for j in range(ilosc_wierzcholkow):
            if macierz_sasiedztwa[i][j] == 1:
                interpretacja_graficzna[i][j] = '1'

    print("\nInterpretacja graficzna:")
    for row in interpretacja_graficzna:
        print(' '.join(row))


graf()