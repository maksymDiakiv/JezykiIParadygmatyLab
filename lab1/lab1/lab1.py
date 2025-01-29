#zad1
# def podzPaczki(wagi, max_waga):
#     for waga in wagi:
#         if waga > max_waga:
#             raise ValueError(f"Paczka o wadze {waga} przekracza maksymalna dozwolona wage kurse ({max_waga} kg)")
#     wagi_sorted = sorted(wagi, reverse= True)
#     kursy = []
#
#     for waga in wagi_sorted:
#         dodano = False
#         for kurs in kursy:
#             if sum(kurs) + waga <= max_waga:
#                 kurs.append(waga)
#                 dodano = True
#                 break
#         if not dodano:
#             kursy.append([waga])
#     return len(kursy), kursy
#
# wagi = [20, 5, 8, 15, 10, 10, 7]
# max_waga = 25
#
# #print(podzPaczki(wagi, max_waga))
# liczba_kursow, kursy = podzPaczki(wagi, max_waga)
# for i, kurs in enumerate (kursy, 1):
#     print(f"Kurs {i}: {kurs} \t suma wagi: {sum(kurs)} kg")

#zad2
graph = {
    '1' : ['2', '3', '5'],
    '2' : ['1', '4'],
    '3' : ['1', '5', '6'],
    '4' : ['2', '7'],
    '5' : ['1', '3', '7'],
    '6' : ['3', '8'],
    '7' : ['4', '5', '8'],
    '8' : ['6', '7']
}


def obliczNajkrSciezke(graph, wierz_pocz, wierz_konc):
    sciezka = []
    visited = []
    
    for wierz_pocz,i in graph:
        if graph[wierz_pocz[i]] not in visited:
            visited.append(graph[wierz_pocz[i]])
            sciezka.append(wierz_pocz)
        else:
            wierz_pocz += 1
            continue

