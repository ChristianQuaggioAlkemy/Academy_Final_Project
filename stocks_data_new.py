from datetime import datetime
from yahoo_fin import stock_info as si
import pandas as pd
import argparse

print('entro in stocks_data_new')

# Creazione dell'argparse
parser = argparse.ArgumentParser(description='Ottieni i dati delle azioni per un determinato codice indice e intervallo di date')
parser.add_argument('index_code', type=str, help='Codice indice per cui recuperare i dati (ad esempio ^GSPC)')
parser.add_argument('start_date', type=str, help="Data di inizio dell'intervallo di date nel formato YYYY-MM-DD")

# Parsing degli argomenti
args = parser.parse_args()
index_code = args.index_code
start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date()
print(index_code)
print(start_date)

# Creazione della funzione per ottenere valori dell'indice/azione 
def get_index_data(index_code, start_date):
    end_date = datetime.today()
    dati_api = si.get_data(index_code, start_date=start_date, end_date=end_date)
    stocks_data = dati_api['adjclose'].reset_index().rename(columns={'index': 'Data'})
    return stocks_data

# Creazione della funzione per ottenere tutti i giorni da una data in input fino al giorno corrente
def get_date_list(start_date):
    end_date = datetime.today()
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    date_df = pd.DataFrame({'Data': date_range})
    date_list = date_df['Data'].tolist()
    return date_list

# Utilizzo delle funzioni con gli input desiderati
stocks_data = get_index_data(index_code, start_date)
date_list = get_date_list(start_date)

# Unire i due DataFrame su 'date'
merged_data = pd.merge(pd.DataFrame({'Data': date_list}), stocks_data, on='Data', how='left')

# Salva il file merged_data
merged_data.to_csv('index_stocks_data.csv', index=False)

print('esco da stocks_data_new')
