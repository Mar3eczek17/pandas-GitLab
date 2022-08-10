# Pandas - Zadanie 2 - Najczęstsze nazwisko
# Osób o jakim nazwisku jest najwięcej ?
import pandas as pd

colnames = ['imię',
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

# print(df)
# Kod 1 type: <class 'pandas.core.series.Series'>
print(df['nazwisko'].mode())
# Kod 2 type: <class 'str'>
print(df['nazwisko'].value_counts().idxmax())
