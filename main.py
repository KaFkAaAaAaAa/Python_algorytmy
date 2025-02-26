def naBin(l):
    b = ""
    while True:
        b = b + str(l % 2)
        l = l // 2
        if l == 0:
            return b[::-1]


print(naBin(10))

plik = open("binarne.txt")
dane = plik.read()
lista = dane.split("\n")
print(lista)


def licztodec(liczba):
    potega = 1
    suma = 0
    while liczba > 0:
        suma = suma + liczba % 10 * potega
        liczba = liczba // 10
        potega = potega * 2
    return suma


ileNiepo = 0
for el in lista:
    dlugosc = len(el)
    segmenty = int(dlugosc / 4)
    lewy = 0
    prawy = 4
    for i in range(segmenty):
        wycinek = el[lewy:prawy]
        if licztodec(int(wycinek)) > 9:
            ileNiepo = ileNiepo + 1
            break
        lewy += 4
        prawy += 4
print("Ilość niepoprawnych", ileNiepo)

maksymalna = 0
binarna = ""
for linia in lista:
    dziesietna = licztodec(int(linia))
    if dziesietna <= 65535 and dziesietna > maksymalna:
        maksymalna = dziesietna
        binarna = linia
print(binarna, maksymalna)