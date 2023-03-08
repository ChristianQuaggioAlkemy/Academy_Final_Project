import pandas as pd
import datetime as dt
from yahoo_fin import stock_info as si

# tramite API scarico il valore dell'indice finanziario SP500 
start_date = dt.datetime(1950,1,1)
end_date = dt.datetime.today()

dati_api = si.get_data('^GSPC',start_date=start_date,end_date=end_date)

#Il valore 'adjclose' rappresenta il valore dell'indice alla chiusura giornaliera del mercato
sp500_data = dati_api['adjclose'].reset_index().rename(columns={'index': 'date'})

# crea una lista di tutte le date dal 1950 ad oggi

df = pd.date_range(start=start_date,end=end_date,freq='D').tolist()
dates = pd.DataFrame({'date':df})


def tronca_data(data):
    return data.split('T')[0]
    
eq = pd.read_csv('earthquakes.csv', sep=',')
eq['Time'] = eq['Time'].apply(tronca_data)

eq = eq.rename(columns={'Time': 'date'})
eq['date'] = pd.to_datetime(eq['date'])


eq = eq.loc[eq.groupby('date')['Mag'].idxmax()]

df_intermedio = pd.merge(dates, sp500_data, on='date', how='left')
df_finale = pd.merge(df_intermedio, eq, on='date', how='left')
df_finale.to_csv()