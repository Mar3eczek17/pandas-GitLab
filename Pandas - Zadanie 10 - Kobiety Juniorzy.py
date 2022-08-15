# Pandas - Zadanie 10 - Kobiety Juniorzy
# Które biuro ma najwięcej kobiet na Juniorskim poziomie doświadczenia ?
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
# Pod to zadanie zmieniono wartości na poniższe, funkcja zwróci takie wartości jak w poniższych komentarzach dla kodu nr 2:
# - Junior (do 14 lat doświadczenia)
# - Mid (15 do 19 lat)
# - Senior (20 do 24 lat)
# - Ekspert (od 25 lat)
import numpy as np
from numpy import nan
Conditions = [(df['doswiadczenie_w_latach'] <= 14),
              (15 <= df['doswiadczenie_w_latach']) & (df['doswiadczenie_w_latach'] <= 19),
             (20 <= df['doswiadczenie_w_latach']) & (df['doswiadczenie_w_latach'] <= 24),
             (25 <= df['doswiadczenie_w_latach'])]
Categories = ['Junior','Mid','Senior','Ekspert']
df['poziom_doświadczenia']=np.select(Conditions, Categories)

# Pandas - Zadanie 10 - Kobiety Juniorzy
# Które biuro ma najwięcej kobiet na Juniorskim poziomie doświadczenia ?
datat = df[(df['poziom_doświadczenia'] == 'Junior') & (df['płeć'] == 'female')].groupby(['miasto_w_którym_znajduje_się_oddział_firmy']).count().imię

# Dla wartości z oryginalnego kodu, funkcja zwróci: Series([], Name: imię, dtype: int64)
# Dla kodu nr 2, funkcja zwróci:
#       miasto_w_którym_znajduje_się_oddział_firmy
#       Krakow    7
#       Name: imię, dtype: int64
datat[datat == datat.max()]
# Dla wartości z oryginalnego kodu, funkcja zwróci: ValueError: attempt to get argmax of an empty sequence
# Dla kodu nr 2, funkcja zwróci: 'Krakow'
datat.idxmax()
