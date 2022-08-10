# Pandas - Zadanie 1 - Dane
# Załaduj zbiór danych korzystajac z biblioteki Pandas. Kolumny w naszym zbiorze danych, to:
# - imię
# - nazwisko
# - rok urodzenia
# - miesiac urodzenia
# - dzień urodzenia
# - miejsce urodzenia
# - miasto, w którym znajduje się oddział firmy
# - departament, w którym pracuje dana osoba
# - rok roczęcia pracy w firmie
# - miesiac rozpoczęcia pracy
# - dzień rozpoczęcia pracy
# - doswiadczenie (w latach)

import pandas as pd

# Nowy DataFrame
df = pd.DataFrame({'imię': [], 
                   'nazwisko': [], 
                   'rok urodzenia': [], 
                   'miesiac urodzenia': [], 
                   'dzień urodzenia': [], 
                   'miejsce urodzenia': [], 
                   'miasto, w którym znajduje się oddział firmy': [],
                   'departament, w którym pracuje dana osoba': [],
                   'rok roczęcia pracy w firmie': [], 
                   'miesiac rozpoczęcia pracy': [], 
                   'dzień rozpoczęcia pracy': [], 
                   'doswiadczenie (w latach)': []})
df
