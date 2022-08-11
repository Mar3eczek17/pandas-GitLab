# Pandas - Zadanie 3 - Płeć
# Po kolumnie z nazwiskiem dodaj kolumnę reprezentującą płeć danej osoby. Można wykorzystać fakt, że imiona
# kobiet kończą się literka 'a'.
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

# adding column using insert() method
df.insert(loc=1, column='płeć', value=df['imię'].str.endswith('a'), allow_duplicates=True)
df

# Metoda zamienająca wartości False,True na male,female
df['płeć'] = df['płeć'].replace([False,True],['male','female'])
df
