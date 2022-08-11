# Pandas - Zadanie 4 - Sortowanie.py
# Posortuj zbiór danych alfabetycznie po nazwiskach, a w ramach jednego nazwiska po roku urodzenia.
import pandas as pd

colnames=['imię', 
          'nazwisko', 
          'rok urodzenia', 
          'miesiac urodzenia',
          'dzień urodzenia', 
          'miejsce urodzenia',
          'miasto, w którym znajduje się oddział firmy',
          'departament, w którym pracuje dana osoba',
          'rok roczęcia pracy w firmie',
          'miesiac rozpoczęcia pracy',
          'dzień rozpoczęcia pracy',
          'doswiadczenie (w latach)']
          
# Wczytywanie pliku CSV
df = pd.read_csv('dataset_pandas_pd.csv', 
                 delimiter=',', 
                 names=colnames)

df

# Sortowanie zbioru danych alfabetycznie po nazwiskach, a w ramach jednego nazwiska po roku urodzenia.
df.sort_values(by=['nazwisko', 'rok urodzenia'], ascending=[True, False])
