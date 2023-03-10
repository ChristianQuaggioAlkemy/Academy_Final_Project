import argparse
import pandas as pd
import datetime as dt
import reverse_geocoder as rg

print('entro in dataset_eq')
# Crea il parser degli argomenti
parser = argparse.ArgumentParser(description='Processa dati dei terremoti')
parser.add_argument('start_date', metavar='YYYY-MM-DD', type=str, help='Data di inizio nel formato YYYY-MM-DD')

# Parsa gli argomenti dalla linea di comando
args = parser.parse_args()

# Converti la data di inizio in formato datetime
start_date = dt.datetime.strptime(args.start_date, '%Y-%m-%d').date()
print(start_date)

# Leggi il file CSV contenente i dati dei terremoti
eq = pd.read_csv('earthquakes.csv')

# Tronca la data e l'ora per mantenere solo la data
eq['Time'] = eq['Time'].apply(lambda x: x.split('T')[0])

# Rinomina la colonna 'Time' in 'date'
eq = eq.rename(columns={'Time': 'Data'})

# Converti la colonna 'date' in formato datetime
eq['Data'] = pd.to_datetime(eq['Data'])

# Seleziona solo il terremoto più forte di ogni giorno
eq = eq.loc[eq.groupby('Data')['Mag'].idxmax()]

# Usa la libreria reverse_geocoder per ottenere tramite API la località e il codice del paese corrispondenti alle coordinate geografiche
locations = list(zip(eq["Latitude"], eq["Longitude"]))
results = rg.search(locations)
eq["Location"] = [result["name"] if result else "Ocean" for result in results]
eq["Country"] = [result["cc"] if result else "NA" for result in results]

# Seleziona solo le colonne necessarie
eq2 = eq[['Data', 'Location', 'Country', 'Latitude', 'Longitude', 'Depth', 'Mag', 'MagType']]

# Crea una lista di tutte le date dal 1990 al giorno corrente
end_date = dt.datetime.today()
dates = pd.date_range(start=start_date, end=end_date, freq='D')
date_df = pd.DataFrame({'Data': dates})

# Unisci i dati dei terremoti con le date
earthquakes_calendar = pd.merge(date_df, eq2, on='Data', how='left')

# Salva i dati creati in un file csv
earthquakes_calendar.to_csv('earthquakes_data.csv', index=False)
print('esco da dataset_eq')

