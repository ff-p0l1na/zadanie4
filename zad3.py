print("Podaj ilość elementów do wysyłki:")
ilosc_elementow = int(input())
suma_wagi_elementow = 0
ilosc_paczek = 0
waga_paczki = 0
for element in range(ilosc_elementow):
    print("Podaj wagę elementu w kg:")
    waga_elementu = float(input())
    suma_wagi_elementow += float(waga_elementu)
    waga_paczki = suma_wagi_elementow
    if waga_paczki > 20:
        suma_wagi_elementow -= float(waga_elementu)
        waga_paczki = float(suma_wagi_elementow)
        ilosc_paczek += 1
        print(f"Wysłano paczkę o wadze {waga_paczki} kg.")
        suma_wagi_elementow = waga_elementu
        continue
        










