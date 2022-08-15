# Pandas - Zadanie 11 - Kobiety Mid
# Ile jest kobiet w krakowskim biurze, na Mid poziomie doświadczenia, urodzonych przed 1975 rokiem ?
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

# Adding column using insert() method
df.insert(loc=1, column='płeć', value=df['imię'].str.endswith('a'), allow_duplicates=True)
df['płeć'] = df['płeć'].replace([False,True],['male','female'])

# Do zbioru danych należy dodać kolumnę, która będzie mówiła o poziomie doświadczenia danej osoby, w sposób
# słowny, przyjmując:
# - Junior (do 3 lat doświadczenia)
# - Mid (4 do 8 lat)
# - Senior (9 do 12 lat)
# - Ekspert (od 13 lat)
import numpy as np
from numpy import nan
Conditions = [(df['doswiadczenie_w_latach'] <= 3),
              (4 <= df['doswiadczenie_w_latach']) & (df['doswiadczenie_w_latach'] <= 8),
             (9 <= df['doswiadczenie_w_latach']) & (df['doswiadczenie_w_latach'] <= 12),
             (13 <= df['doswiadczenie_w_latach'])]
Categories = ['Junior','Mid','Senior','Ekspert']
df['poziom_doświadczenia']=np.select(Conditions, Categories)

# Pandas - Zadanie 11 - Kobiety Mid
# Ile jest kobiet w krakowskim biurze, na Mid poziomie doświadczenia, urodzonych przed 1975 rokiem ?
data = df[(df['poziom_doświadczenia'] == 'Mid') & (df['płeć'] == 'female') 
         & (df['rok_urodzenia'] < 1975)].count().imię
data
