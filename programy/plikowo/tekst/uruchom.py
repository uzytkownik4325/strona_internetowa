from tekst import *

tekst = Tekst()
tekst.ustaw("Siała baba mak mak mak mak.")
tekst.wyswietl()
dlugosc = tekst.zwroc_dlugosc()
print(dlugosc)
fragment = tekst.zwroc_fragment(0, 5)
print(fragment)
indeks = tekst.znajdz("mak")
print(indeks)
indeks = tekst.znajdz_od("a", 5)
print(indeks)
indeks = tekst.znajdz_od_do("a", 5, 12)
print(indeks)
indeksy = tekst.znajdz_wszystkie("mak mak")
print(indeksy)
indeksy = tekst.znajdz_wszystkie_od("a", 5)
print(indeksy)
indeksy = tekst.znajdz_wszystkie_od_do("a", 5, 13)
print(indeksy)
