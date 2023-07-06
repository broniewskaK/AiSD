import math

def znajdz_najkrotsza_droge(graf, start, koniec):
    odleglosci = {wierzcholek: math.inf for wierzcholek in graf}
    odleglosci[start] = 0
    poprzednicy = {}

    nieodwiedzone_wierzcholki = set(graf)

    while nieodwiedzone_wierzcholki:
        aktualny = min(nieodwiedzone_wierzcholki, key=lambda w: odleglosci[w])
        nieodwiedzone_wierzcholki.remove(aktualny)
        if aktualny == koniec:

            sciezka = []
            while aktualny in poprzednicy:
                sciezka.insert(0, aktualny)
                aktualny = poprzednicy[aktualny]
            sciezka.insert(0, start)
            return sciezka

        for sasiad, waga in graf[aktualny].items():
            nowa_odleglosc = odleglosci[aktualny] + waga
            if nowa_odleglosc < odleglosci[sasiad]:
                odleglosci[sasiad] = nowa_odleglosc
                poprzednicy[sasiad] = aktualny
    return None
graf = {
    'A': {'B': 4, 'C': 2},import math

def znajdz_najkrotsza_droge(graf, start, koniec):
    odleglosci = {wierzcholek: math.inf for wierzcholek in graf}
    odleglosci[start] = 0
    poprzednicy = {}

    nieodwiedzone_wierzcholki = set(graf)

    while nieodwiedzone_wierzcholki:
        aktualny = min(nieodwiedzone_wierzcholki, key=lambda w: odleglosci[w])
        nieodwiedzone_wierzcholki.remove(aktualny)
        if aktualny == koniec:

            sciezka = []
            while aktualny in poprzednicy:
                sciezka.insert(0, aktualny)
                aktualny = poprzednicy[aktualny]
            sciezka.insert(0, start)
            return sciezka

        for sasiad, waga in graf[aktualny].items():
            nowa_odleglosc = odleglosci[aktualny] + waga
            if nowa_odleglosc < odleglosci[sasiad]:
                odleglosci[sasiad] = nowa_odleglosc
                poprzednicy[sasiad] = aktualny
    return None
graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 4, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 6, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

pierwszy = 'A'
ostatni = 'E'

najkrotsza_droga = znajdz_najkrotsza_droge(graf, pierwszy, ostatni)

if najkrotsza_droga:
    print("Najkrótsza droga:", ' -> '.join(najkrotsza_droga))
else:
    print("Nie istnieje droga między początkiem, a końcem.")
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 4, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 6, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

pierwszy = 'A'
ostatni = 'E'

najkrotsza_droga = znajdz_najkrotsza_droge(graf, pierwszy, ostatni)

if najkrotsza_droga:
    print("Najkrótsza droga:", ' -> '.join(najkrotsza_droga))
else:
    print("Nie istnieje droga między początkiem, a końcem.")