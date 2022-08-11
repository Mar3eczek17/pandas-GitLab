# Pandas - Zadanie 5 - Doświadczenie

# Do zbioru danych należy dodać kolumnę, która będzie mówiła o poziomie doświadczenia danej osoby, w sposób
# słowny, przyjmując:

# - Junior (do 3 lat doświadczenia)
# - Mid (4 do 8 lat)
# - Senior (9 do 12 lat)
# - Ekspert (od 13 lat)
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

# Do zbioru danych należy dodać kolumnę, która będzie mówiła o poziomie doświadczenia danej osoby, w sposób
# słowny, przyjmując:
# - Junior (do 3 lat doświadczenia)
# - Mid (4 do 8 lat)
# - Senior (9 do 12 lat)
# - Ekspert (od 13 lat)
import numpy as np
Conditions = [(df['doswiadczenie (w latach)'] <= 3),
              (4 <= df['doswiadczenie (w latach)']) & (df['doswiadczenie (w latach)'] <= 8),
             (9 <= df['doswiadczenie (w latach)']) & (df['doswiadczenie (w latach)'] <= 12),
             (13 <= df['doswiadczenie (w latach)'])]
Categories = ['Junior','Mid','Senior','Ekspert']
df['poziom doświadczenia']=np.select(Conditions, Categories)
df
