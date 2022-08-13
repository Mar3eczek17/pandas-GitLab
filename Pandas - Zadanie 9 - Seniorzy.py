# Pandas - Zadanie 9 - Seniorzy
# Które biuro firmy ma najwięcej osób na Seniorskim poziomie doświadczenia ?
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

import numpy as np
from numpy import nan
Conditions = [(df['doswiadczenie_w_latach'] <= 3),
              (4 <= df['doswiadczenie_w_latach']) & (df['doswiadczenie_w_latach'] <= 8),
             (9 <= df['doswiadczenie_w_latach']) & (df['doswiadczenie_w_latach'] <= 12),
             (13 <= df['doswiadczenie_w_latach'])]
Categories = ['Junior','Mid','Senior','Ekspert']
df['poziom_doświadczenia']=np.select(Conditions, Categories)

# Które biuro firmy ma najwięcej osób na Seniorskim poziomie doświadczenia ?
data = df[df[
              'poziom_doświadczenia'] == 'Senior'].groupby([
    'miasto_w_którym_znajduje_się_oddział_firmy']).count().poziom_doświadczenia
data[data == data.max()]
data.idxmax()
