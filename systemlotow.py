# Lista dostępnych lotów 
loty = [
    {"id": 1, "nazwa": "Warszawa - Nowy Jork", "dostepne_miejsca": 10},
    {"id": 2, "nazwa": "Kraków - Londyn", "dostepne_miejsca": 5},
    {"id": 3, "nazwa": "Gdańsk - Berlin", "dostepne_miejsca": 20}
]


pasazerowie = []


def wyswietl_loty():
    print("Dostępne loty:")
    for lot in loty:
        print(f"ID: {lot['id']} | Trasa: {lot['nazwa']} | Dostępne miejsca: {lot['dostepne_miejsca']}")


def rezerwuj_bilet():
    wyswietl_loty()
    lot_id = int(input("Wybierz ID lotu: "))
    
    #wyszukaj lot po ID
    lot = next((lot for lot in loty if lot["id"] == lot_id), None)
    
    if lot:
        if lot["dostepne_miejsca"] > 0:
            imie = input("Podaj imię pasażera: ")
            nazwisko = input("Podaj nazwisko pasażera: ")
            pasazerowie.append({"imie": imie, "nazwisko": nazwisko, "lot_id": lot_id})
            lot["dostepne_miejsca"] -= 1
            print(f"Rezerwacja dla {imie} {nazwisko} została pomyślnie dokonana na lot {lot['nazwa']}.")
        else:
            print("Brak dostępnych miejsc na tym locie.")
    else:
        print("Nie znaleziono lotu o podanym ID.")

# Funkcja do wyświetlania listy pasażerów
def wyswietl_pasażerów():
    if pasazerowie:
        print("\nLista pasażerów:")
        for pasazer in pasazerowie:
            lot = next((lot for lot in loty if lot["id"] == pasazer["lot_id"]), None)
            print(f"{pasazer['imie']} {pasazer['nazwisko']} - Lot: {lot['nazwa']}")
    else:
        print("Brak pasażerów w systemie.")


def main():
    while True:
        print("\n--- System Rezerwacji Biletów Lotniczych ---")
        print("1. Wyświetl dostępne loty")
        print("2. Zarezerwuj bilet")
        print("3. Wyświetl listę pasażerów")
        print("4. Zakończ")
        
        wybor = input("Wybierz opcję (1/2/3/4): ")
        
        if wybor == "1":
            wyswietl_loty()
        elif wybor == "2":
            rezerwuj_bilet()
        elif wybor == "3":
            wyswietl_pasażerów()
        elif wybor == "4":
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
