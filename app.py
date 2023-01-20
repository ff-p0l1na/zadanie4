#zmienne
liczba_elementow_do_wyslania =
waga_aktualnego_elementu =
liczba_paczek_wyslanych = 0
liczba_kg_wyslanych = 0
waga_najlzejszej_paczki = 20
nr_najlzejszej_paczki = None
waga_aktualnej_paczki =

#restrykcje
1 <= waga_aktualnego_elementu <= 10
waga_aktualnej_paczki <= 20

#pseudokod
"""
1. do zmiennej liczba_elementow_do_wyslania wczytaj podana przez usera liczbe elementow
2. dla kazdego elementu z zakresu liczba_elementow_do_wyslania:
- do zmiennej waga aktualnego elementu wczytaj wage elementu podana przez usera
- jesli waga elementu nie jest w zakresie 1-10:
     -przerwij wczytywanie elementow
- dodaj wage aktualnego elementu do wagi aktualnej paczki
- jesli waga aktualnej paczki > 20:
    -odejmij waga aktualnego elementu od wagi aktualnej paczki
    -dodaj 1 do liczba paczek wyslanych (wyslij paczke)
    - jesli waga aktualnej paczki jest mniejsza od waga najlzejszej paczki:
         -do wagi najlzejszej paczki zapisz waga aktualnej paczki
         - do nr najlzejszej paczki zapisz liczbe paczek wyslanych
    - do liczby kg wyslanych doaj waga aktualnej paczki
    - zapisz do waga aktualnej paczki = waga aktualnego elementu
- jesli waga aktualnej paczki jest rowna 20
    - dodaj 1 do liczby pazek wyslanych
    - do liczby kg wyslanych dodaj wage aktualnej paczki
    - zapisz do wagi aktualnej paczki wartosc 0
- jesli waga aktualnej paczki < 20:
    - nic nie rob
    
3. Jesli waga aktualnej paczki > 0:
- dodaj 1 do liczby paczek wyslanych
- do liczby kg wyslanych dodaj wage aktualnej paczki

4. Wypisz:
- liczba paczek wyslanych
- liczba kg wyslanych
- liczba paczek wyslanych * 20 - liczba kg wyslanych
- 


"""
