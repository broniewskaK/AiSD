def odwrocona(tab):
    if len(tab) <= 1:
        return tab
    else:
        return [tab[-1]] + odwrocona(tab[:-1])

tab1 = [1, 2, 3, 4, 5]
odwrocona = odwrocona(tab1)
print(odwrocona)