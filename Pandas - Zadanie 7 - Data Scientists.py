# Pandas - Zadanie 7 - Data Scientists
# Który oddział firmy ma najwięcej Data Scientistów ?
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

# Pandas - Zadanie 7 - Data Scientists
# Który oddział firmy ma najwięcej Data Scientistów ?
data = df[df['departament, w którym pracuje dana osoba'] == 'Data Science'].groupby(['miasto, w którym znajduje się oddział firmy', 'departament, w którym pracuje dana osoba']).count().imię

# Return (miasto, w którym znajduje się oddział firmy, departament, w którym pracuje dana osoba, count)
data[data == data.max()]

# Return tuple ('City', 'Departament')
data.idxmax()
