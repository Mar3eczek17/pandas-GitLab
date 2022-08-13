# Pandas - Zadanie 8 - Nazwy departamentów

# Szef chciałby zmienić nazewnictwo departamentów w całej firmie. Napisz kod, który zamieni wartości w
# kolumnie reprezentującej departament, nastepująco:

#     - Software Development -> Software Development Team
#     - HR -> Human Resources
#     - Data Science -> Data Analytics
import pandas as pd

colnames=['imię', 
          'nazwisko', 
          'rok_urodzenia', 
          'miesiac_rodzenia',
          'dzień_rodzenia', 
          'miejsce_rodzenia',
          'miasto_w_którym_znajduje_się_oddział_firmy',
          'departament_w_którym_pracuje_dana_osoba',
          'rok_roczęcia_pracy_w_firmie',
          'miesiac_rozpoczęcia_pracy',
          'dzień_rozpoczęcia_pracy',
          'doswiadczenie_w_latach']
          
# Wczytywanie pliku CSV
df = pd.read_csv('dataset_pandas_pd.csv', 
                 delimiter=',', 
                 names=colnames)

# Zadanie 8
# Zmiana nazewnictwa departamentów w całej firmie. Zamiana wartości w kolumnie reprezentującej departament, nastepująco:
# - Software Development -> Software Development Team
# - HR -> Human Resources
# - Data Science -> Data Analytics
df.replace(
    {"HR": "Human Resources", 'Data Science': 'Data Analytics', 'Software Development': 'Software Development Team'},
    inplace=True)
df
