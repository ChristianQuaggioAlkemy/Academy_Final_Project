from datetime import datetime
from yahoo_fin import stock_info as si
import pandas as pd

# Creazione della funzione per ottenere valori dell'indice/azione 
def get_index_data(index_code, start_date):
    end_date = datetime.today()
    dati_api = si.get_data(index_code, start_date=start_date, end_date=end_date)
    stocks_data = dati_api['adjclose'].reset_index().rename(columns={'index': 'date'})
    return stocks_data

# Creazione della funzione per ottenere tutti i giorni da una data in input fino al giorno corrente
def get_date_list(start_date):
    end_date = datetime.today()
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    date_df = pd.DataFrame({'date': date_range})
    date_list = date_df['date'].tolist()
    return date_list

# Utilizzo delle funzioni con gli input desiderati
index_code = '^GSPC'
start_date = datetime.strptime('1950-01-01', '%Y-%m-%d').date()

stocks_data = get_index_data(index_code, start_date)
date_list = get_date_list(start_date)

# Unire i due DataFrame su 'date'
merged_data = pd.merge(pd.DataFrame({'date': date_list}), stocks_data, on='date', how='left')

# sostituisci i valori nulli in adjclose con il valore della riga precedente
merged_data["adjclose"].fillna(method="ffill", inplace=True)

# elimina le righe con valori nulli nella colonna "adjclose"
merged_data.dropna(subset=["adjclose"], inplace=True)

# seleziona solo le righe a partire dalla prima con valori non nulli
merged_data = merged_data.iloc[merged_data["adjclose"].first_valid_index():]

# calcola la variazione tra il valore di adjclose di un determinato giorno e il valore adjclose del giorno precedente
merged_data["adjclose variation"] = (merged_data["adjclose"] - merged_data["adjclose"].shift(1)) / merged_data["adjclose"].shift(1)

# Crea una nuova colonna 'weekday' che contiene il giorno della settimana come intero (lunedì=0, martedì=1, ecc.)
merged_data['weekday'] = merged_data['date'].dt.weekday

# Crea colonne dummy per la colonna 'weekday'
dummy_cols = pd.get_dummies(merged_data['weekday'], prefix='dum')

# Aggiungi le colonne dummy al dataframe
merged_data = pd.concat([merged_data, dummy_cols], axis=1)

# Elimina le colonne relative a sabato e domenica
merged_data.drop(['dum_5', 'dum_6'], axis=1, inplace=True)

# Sostituisce il nome delle colonne dummy
merged_data = merged_data.rename(columns={'dum_0': 'dum_mon', 'dum_1': 'dum_tue', 'dum_2': 'dum_wed', 'dum_3': 'dum_thu', 'dum_4': 'dum_fri'})

# Elimina la colonna weekday che non è più necessaria
merged_data = merged_data.drop('weekday', axis=1)

# Salva il file merged_data
merged_data.to_csv('index_stocks_data.csv', index=False)