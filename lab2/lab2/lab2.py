
from functools import reduce
import re
# listaA = [1,2,3,4,5,6,7,56,4,43]
# listaB = [x**2 for x in listaA if x % 2 ==0]
# print(listaB)

#map
# listaC = list(map(lambda x: x ** 2, listaA))
#print(listaC)

#filter
# listaD = list(filter(lambda x : x % 2 == 0, listaC))
#print(listaD)

#reduce
#listaE = reduce(lambda x, y : x + y, listaD)
#print(listaE)

# tekst = """listaE = reduce(lambda x, y : x + y, listaD)
# print(listaE)"""

#exec(tekst)

#print(eval("1+1"))

tekst = "Zlicza liczbę słów, zdań, i akapitów w tekście.Wyszukuje najczęściej występujące słowa, wykluczając tzw. stop words (np. 'i', 'a', 'the')."
def zad1(tekst):
    # paragraf = len(list(filter(lambda x: x == "\n", tekst)))

    paragraf1 = [p for p in tekst.strip().split('\n') if p]
    iloscParagr = len(paragraf1)
    #print(iloscParagr)

    zdan = len(list(filter(lambda x: x == "." or x == "?" or x =="!", tekst)))
    zdan2 = re.split(r'[.!?]', tekst)
    zdan3 = [tekst.strip() for tekst in zdan2 if tekst.strip()]
    ilosczdan3 = len(zdan3)

    teks1 = [[ reversed(t) for t in tekst.split() if t.startswith('a') or t.startswith('A') ]]
    print(teks1)


zad1(tekst)

