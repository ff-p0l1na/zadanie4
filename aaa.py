liczba_paczek_wyslanych = 0
liczba_kg_wyslanych = 0
suma = 0
print("Podaj liczbę elementów do wysyłki:")
ilosc_elementow = int(input())
while ilosc_elementow > 0:
    print("Podaj wagę elementu w kg:")
    waga_elementu = float(input())
    suma += float(waga_elementu)
    ilosc_elementow -= 1
    liczba_kg_wyslanych += float(waga_elementu)
    if float(suma) > 20:
        liczba_paczek_wyslanych += 1
        suma -= float(waga_elementu)
        liczba_kg_wyslanych -= float(waga_elementu)
        paczka = float(suma)
        print(f"""Przekroczono dopuszczalną wagę paczki. 
Wysyłam paczkę o wadze {paczka} kg i dodaję ostatni element do kolejnej paczki."""
              .format(float(paczka)))
        paczka -= float(waga_elementu)
        continue
    if float(suma) <= 20:
        continue
print(liczba_kg_wyslanych)
print(liczba_paczek_wyslanych)
