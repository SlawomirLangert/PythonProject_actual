import requests
import pandas as pd
from pandas.io.formats.format import return_docstring
import time
# from tqdm import tqdm
# # Procenty są wyświetlane automatycznie po prawej stronie
# for i in tqdm(range(100), desc="Przetwarzanie"):
#     time.sleep(0.05)

from config import Config
pd.set_option('display.max_columns', None)                # ustawienie globalne dla DataFrame, aby wyswietlalo wszystkie kolumny
pd.set_option('display.width', None)                      # ustawienie globalne dla DataFrame, aby wyswietlalo cala szerokosc (zawartosc) kolumny

lm = Config().limit_pokemon                                     # lm = limit pokemonow pobranych z Config (wpisane recznie)
lista_pokemonow = []                                            # przygotowanie pustej nowa liste pokemonow (lista glowna)

# start:  ======================= def funkcje

def zeruj_lilste ():                                            # wywolanie funkcji usuwajace zawratosc listy
    return lista_pokemonow.clear()                              # zwraca pusta liste glowna (przygotowanie do wywolania kolejnych funkcji)

def wszystkie_pokemony():                                       # utworzenie funkcji ktora jest uruchamiana w pliku main
   try:
     url = f"https://pokeapi.co/api/v2/pokemon?limit={lm}"      # wstawienie zmiennej lm do linku dynamicznie
     print(f"Aktualny limit wyswietlanych wartosci to: {lm}")   # wyswietlanie aktualnej wartosci limitu

     response = requests.get(url)                               # sprawdzenie poprawnosci odpowiedzi (uzycia) linku url
     print(f"status odpowiedzi: {response.status_code}")        # pobranie statusu odpowiedzi na link powyzej
     dane = response.json()                                     # pobranie calej listy z linku
    # print(dane)                                               # wyswietenie (sprawdzenie) zawartosci slownik z linku
    # print(dane.get("results"))                                # wyswietlenie zawartosci tylko slownika -lista "result"

     for x in range(len(dane.get("results"))):                  # przejdz przez kazda wartosc w liscie o dlugosci listy "result"
         nowy = {                                               # utworz nowa liste
         "nazwa_pokemona" : dane.get("results")[x].get("name"), # dodaj nazwe pokemona w nowej liscie "lista pokemonow"
         "link_pokemona" : dane.get("results")[x].get("url")    # dodaj url pokemona w nowej liscie "lista pokemonow"
         }
         lista_pokemonow.append(nowy)                           # dodaj kolejna wartosc do nowego slownika
     return lista_pokemonow                                     # zwroc cala wartosc listy (slownik: nazwa + url)
   except Exception as e:                                       # przejecie bledu wyswietenie bledu, jesli wystapi
       print(e)                                                 # wyswietlenie bledu wyswietenie bledu, jesli wystapi

def id_pokemona():
     try:
         lista_pokemonow_id = []                                # przygotowanie pustej nowa liste pokemonow (lista pomocnicza)
         wynik_id = wszystkie_pokemony()                        # przypisanie do zmiennej bazowej listy pokemonow i wywolanie 1. funkcji (tworzenie bazowej listy pokemonow)
        # print(f"wynik_id:  {wynik_id}")
         for x in range(len(wynik_id)):                         # petla for (od 0 do dlugosci tabeli)
            #  print(f"co tu jest: {wynik_id[x]}")
              url = f"https://pokeapi.co/api/v2/pokemon/{x+1}"  # przypisanie do url zmiennej liczbowej (biezacej) +1
            #  print(url)
              response = requests.get(url)                      # sprawdzenie czy url istnieje i przypisanie odpowiedzi do zmiennej
             # print(f"response: {response}")
              dane = response.json()                            # przypisanie do zmiennej odpowiedzi, ktora jest lista/slownikiem (otrzymany/pobrany od url)
            #  print(f"status odpowiedzi: {response.status_code}")
            #  print(f"dane: {dane.get('id')}")
              nowy = {                                                  # utworzenie nowej slownika
                "nazwa_pokemona": wynik_id[x].get("nazwa_pokemona"),    # wypelnianie slownika danymi: klucz -> nazwa bazowa w slowniku | wartosc -> wypelnianie wartoscia z indexem x pobrana z nowej listy
                "link_pokemona": wynik_id[x].get("link_pokemona"),
                "id_pokemona" : dane.get("id")                          # wypelnienie slownika nowymi danymi pobrane z podstrony (z poziomu nizej)
              }
             # print(f"nowy: {nowy}")
              lista_pokemonow_id.append(nowy)                           # aktualizacja listy nowymi danymi

         lista_pokemonow.extend(lista_pokemonow_id)                     # laczenie dwol list (utworzonej z 1 funkcji z nowa lista z nowymi danymi)
         return lista_pokemonow_id                                      # zwracana wartosc listy (by mogla byc uzyta do tworzenia DataFrame)
     except Exception as e:
           print(e)


def typ_pokemona():
    try:
        lista_pokemonow_types = []                                             # przygotowanie pustej nowa liste pokemonow (lista pomocnicza)
        wynik_types = id_pokemona()                                         # przypisanie do zmiennej bazowej listy pokemonow i wywolanie 1. funkcji (tworzenie bazowej listy pokemonow)
        nowy_types = {} #wynik
       # typ_pokemona = {}
        test_typu = []
        klucz = "typy pokemona"
       # print(f"wynik_types:  {wynik_types}")
       #  if klucz not in typ_pokemona:
       #       typ_pokemona[klucz] = []

        for x in range(len(wynik_types)):                                    # petla for (od 0 do dlugosci tabeli)
           # print(f"co tu jest: {wynik_types[x]}")
            url = f"https://pokeapi.co/api/v2/pokemon/{x + 1}"               # przypisanie do url zmiennej liczbowej (biezacej) +1
            #  print(url)
            response = requests.get(url)                                     # sprawdzenie czy url istnieje i przypisanie odpowiedzi do zmiennej
            # print(f"response: {response}")
            dane = response.json()                                           # przypisanie do zmiennej odpowiedzi, ktora jest lista/slownikiem (otrzymany/pobrany od url)
           # print(f"status odpowiedzi: {response.status_code}")

           # print(f"dane[types] x: {x} : {dane.get("types")}\n")
            nowy_types[x] = dane.get("types")                                  # utworzenie tablicy z wartosciami "types"

            for y in range(len(nowy_types)):                                    # petla for I rzedu : pierwszy index tablicy [y][]
                test_typu = []                                                  # wyczyszczenie zawartosci listy
               #print(f"przed for z: typ pusty {test_typu}")
                for z in range(len(nowy_types[y])):                             # petla for II rzedu : drugi index tablicy [][z]
                   typ = nowy_types[y][z].get("type").get("name")               # utworzenie zmiennej listy z wartosciami "nazwami typow pokemona" z podwojnym slownikiem {y}{z}
                 # print(f"y {y} z {z}")
                 # print(f"nowy_types[{y}][{z}] {nowy_types[y][z]} typ: {typ}")
                   #test_typu = typ
                   test_typu.append(typ)                                        # dodanie wartosci z kolejnych slownikow (tworzenie listy ["",""]
                   #typ_pokemona[klucz].append(typ)
                 # print(f"test_typu {test_typu}")
            nowy = {                                                            # utworzenie nowego slownika z indexem x = id pokemona, dodanie klucza typ_pokemona (lista)
             "nazwa_pokemona": wynik_types[x].get("nazwa_pokemona"),
             "link_pokemona": wynik_types[x].get("link_pokemona"),
             "id_pokemona": dane.get("id"),
             "typ_pokemona": test_typu,
            }
            lista_pokemonow_types.append(nowy)                                  # dodanie kolejnych wartosci "nowy" do slownika (kolejne pokemony wzgl id)
      # print(f"lista_pokemonow_types {lista_pokemonow_types}")
      # print(f"po for y: typ pelny {test_typu}")

        lista_pokemonow.extend(lista_pokemonow_types)                           # rozszerzenie (laczenie) glownego slownika w calosc
        return lista_pokemonow_types                                            # zwracana wartosc listy (by mogla byc uzyta do tworzenia DataFrame)
    except Exception as e:
        print(e)


def attack_defense_pokemona():
    try:
        lista_pokemonow_attack_defence = []                                                      # przygotowanie pustej nowa liste pokemonow (lista pomocnicza)
        wynik_atak_obrona = typ_pokemona()                                              # przypisanie do zmiennej bazowej listy pokemonow i wywolanie 1. funkcji (tworzenie bazowej listy pokemonow)
        # print(f"wynik_id:  {wynik_id}")
        for x in range(len(wynik_atak_obrona)):                                               # petla for (od 0 do dlugosci tabeli)
            #  print(f"co tu jest: {wynik_id[x]}")
            url = f"https://pokeapi.co/api/v2/pokemon/{x + 1}"                       # przypisanie do url zmiennej liczbowej (biezacej) +1
            #  print(url)
            response = requests.get(url)                                             # sprawdzenie czy url istnieje i przypisanie odpowiedzi do zmiennej
            # print(f"response: {response}")
            dane = response.json()                                                   # przypisanie do zmiennej odpowiedzi, ktora jest lista/slownikiem (otrzymany/pobrany od url)
            #  print(f"status odpowiedzi: {response.status_code}")
            #  print(f"dane: {dane.get('id')}")

            nowy = {                                                                  # utworzenie nowej slownika
                 "nazwa_pokemona": wynik_atak_obrona[x].get("nazwa_pokemona"),                 # wypelnianie slownika danymi: klucz -> nazwa bazowa w slowniku | wartosc -> wypelnianie wartoscia z indexem x pobrana z nowej listy
                 "link_pokemona": wynik_atak_obrona[x].get("link_pokemona"),
                 "id_pokemona": dane.get("id"),                                        # wypelnienie slownika nowymi danymi pobrane z podstrony (z poziomu nizej)
                 "atak": dane.get("stats")[1].get("base_stat"),
                 "obrona": dane.get("stats")[2].get("base_stat")
            }
            lista_pokemonow_attack_defence.append(nowy)                                           # aktualizacja listy nowymi danymi


        lista_pokemonow.extend(lista_pokemonow_attack_defence)                                                       # laczenie dwol list (utworzonej z 1 funkcji z nowa lista z nowymi danymi)
        return lista_pokemonow_attack_defence                                                     # zwracana wartosc listy (by mogla byc uzyta do tworzenia DataFrame)
    except Exception as e:
        print(e)


# koniec:  ======================= def funkcje





# start:  ======================= slownik_glowny

def slownik_glowny(wybor):
    try:
       match int(wybor):
             case 1:
                 start = time.perf_counter()                                                     # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 1. - Pobierz pierwsze 20 Pokémonów i zapisz ich nazwy do listy oraz Pandas DataFrame.")
                 wynik = wszystkie_pokemony()                                                    # wywolaj funkcje i przypisz zwracana wartosc do zmiennej
                 print(f"Wynik utworzonej listy z elementatmi slownika: \n {wynik} \n")          # wyswietlenie zwroconej listy z funkcji
                 df = pd.DataFrame(wynik)                                                        # utworz zmienna df DataFrame z otrzymanej listy "wynik"
                 print(f"{df}\n")                                                                # wyswietl df w postaci tabeli
                 stop = time.perf_counter()                                                      # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()
                 return menu()
             case 2:
                 start = time.perf_counter()                                                   # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 2. - Dla każdego z tych Pokémonów pobierz jego id i dodaj jako nową kolumnę do DataFrame.")
                 wynik_id = id_pokemona()                                                       # wywolaj funkcje i przypisz zwracana wartosc do zmiennej
                 df = pd.DataFrame(wynik_id)                                                    # utworz zmienna df DataFrame z otrzymanej listy "wynik_id"
                 print(f"{df}\n")                                                               # wyswietl df w postaci tabeli
                # id_pokemona()

                # df = pd.DataFrame(wynik_id)
                # print(f"{df}\n")
                 stop = time.perf_counter()                                                     # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()                                                                 # wywolaj funkcje usuwajaca cala zawartosc glownego slownika
                 return menu()
             case 3:
                 start = time.perf_counter()                                                    # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 3. - Pobierz typy (np. fire, water, grass) dla każdego z tych Pokémonów i dodaj jako kolumnę \n"
                       "types (jeśli mają więcej niż jeden typ – zapisz jako listę/string).")
                 #typ_pokemona()
                 wynik_types = typ_pokemona()                                                   # wywolaj funkcje i przypisz zwracana wartosc do zmiennej
                 df = pd.DataFrame(wynik_types)                                                 # utworz zmienna df DataFrame z otrzymanej listy "wynik_types"
                 print(f"{df}\n")                                                               # wyswietl df w postaci tabeli
                 stop = time.perf_counter()                                                     # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()                                                                 # wywolaj funkcje usuwajaca cala zawartosc glownego slownika
                 return menu()
             case 4:
                 start = time.perf_counter()                                                    # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 4. - Wyświetl tylko te Pokémony, które mają typ 'water'")
                 wynik_water = typ_pokemona()
                 df = pd.DataFrame(wynik_water)                                                  # utworz zmienna df DataFrame z otrzymanej listy "wynik_types"
                 print(f"{df}\n")                                                                # wyswietl df w postaci tabeli
                 water = df[df['typ_pokemona'].apply(lambda x: "water" in x)]                    # Filtrowanie DataFrame przy użyciu lambda - Wybieramy tylko te wiersze, gdzie w nazwie produktu występuje "water"

                 print(f"{water}\n")


                 stop = time.perf_counter()                                                      # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()                                                                  # wywolaj funkcje usuwajaca cala zawartosc glownego slownika
                 return menu()
             case 5:
                 start = time.perf_counter()                                                     # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 5. - Dla tych Pokémonów pobierz attack i defense i dodaj je jako kolumny do DataFrame.")

                # wynik_water = typ_pokemona()
                 # df = pd.DataFrame(wynik_water)                                                  # utworz zmienna df DataFrame z otrzymanej listy "wynik_types"
                 # print(f"{df}\n")                                                                # wyswietl df w postaci tabeli
                 # water = df[df['typ_pokemona'].apply(lambda x: "water" in x)]                    # Filtrowanie DataFrame przy użyciu lambda - Wybieramy tylko te wiersze, gdzie w nazwie produktu występuje "water"

                 # print(f"{water}\n")
                 # print(f"{type(water)}\n")

                 wynik_attack_defense = attack_defense_pokemona()
                 df = pd.DataFrame(wynik_attack_defense)
                 print(f"{df}\n")

                 stop = time.perf_counter()                                                      # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()                                                                   # wywolaj funkcje usuwajaca cala zawartosc glownego slownika
                 return menu()
             case 6:
                 start = time.perf_counter()                                                      # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 6. - Oblicz średnie wartości attack i defense dla wszystkich Pokémonów z listy.")

                 wynik_attack_defense = attack_defense_pokemona()
                 df = pd.DataFrame(wynik_attack_defense)
                #df['srednia_wynikow'] = df[['atak', 'obrona']].mean(axis=1)                   # obliczenie srednich wartosci 'atak' i 'obrona' pokemona (z uwgzlednieniem osi)
                 #axis=0 (domyślne): Oblicza średnią pionowo (z góry na dół). Wynikiem jest jedna wartość dla całej kolumny.
                 #axis=1: Oblicza średnią poziomo (od lewej do prawej). Wynikiem jest średnia dla każdego wiersza osobno.

                 df['srednia_wynikow'] = (df['atak'] + df['obrona']) / 2                        # obliczenie srednich wartosci 'atak' i 'obrona' pokemona

                 print(f"{df}\n")

                 stop = time.perf_counter()  # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()  # wywolaj funkcje usuwajaca cala zawartosc glownego slownika

                 return menu()
             case 7:
                 start = time.perf_counter()  # Start pomiaru przed wywołaniem
                 print("TRESC ZAD 7. - Posortuj DataFrame malejąco według attack i wyświetl 5 najsilniejszych Pokémonów.")

                 wynik_attack_defense = attack_defense_pokemona()
                 df = pd.DataFrame(wynik_attack_defense)
                 df['srednia_wynikow'] = (df['atak'] + df['obrona']) / 2                                # obliczenie srednich wartosci 'atak' i 'obrona' pokemona
                 max_5 = df.sort_values(by='srednia_wynikow').nlargest(5,'srednia_wynikow')  # przypisanie do zmiennej najwiekszych 5 wynikow z kol. srednia wynikow pokemona
                 #df.nlargest(5, 'srednia_wynikow')

                 print(f"{max_5}\n")                                                                     # wyswietlenie tabeli DataFrame

                 stop = time.perf_counter()  # Koniec pomiaru
                 print(f"Czas operacji: {stop - start:.8f} s\n")

                 zeruj_lilste()  # wywolaj funkcje usuwajaca cala zawartosc glownego slownika

                 return menu()
             case 8:
                 print(f"Zakończyłeś działanie programu. \n Dziękuję za użycie programu")
             case _:
                 print(f"Wybrałeś liczbę mniejszą niż 1 i większą niż 8. Popraw się.\n\n")
                 return menu()
    except Exception as e:
     print(f"Wpisałeś/aś wartość niebędącą liczbą z zakresu 1-8. Popraw się. \n"
           f"Błąd: {e}\n")
     return menu()

# koniec: ======================= slownik_glowny

# start:  ======================= menu

def menu():
    print (f"Zad 1: Pobieranie nazw Pokémonów: \n"
           f"Zad 2: Dodanie ID Pokémonów: \n"
           f"Zad 3: Typy Pokémonów: \n"
           f"Zad 4: Filtracja po typie: \n"
           f"Zad 5: Statystyki ataku i obrony: \n"
           f"Zad 6: Średni atak i obrona: \n"
           f"Zad 7: Sortowanie po ataku: \n"           
           f"    8: Zakończ: ")
    wybor_operacji = input("Wpisz swój wybór: ")
    print(f"Wybrałeś {wybor_operacji}")
    slownik_glowny(wybor_operacji)

# koniec: ======================= menu


menu()                                                      # Początek programu