import pandas as pd
from countryinfo import CountryInfo

# Leggi il file di input
input_data = pd.read_csv('country_codes.csv')

# Crea una nuova colonna 'population' e 'urban_density'
input_data['population'] = None
input_data['urban_density'] = None

# Loop sui dati e ottieni le informazioni sui paesi
for i, row in input_data.iterrows():
    code = row['code']
    country = row['country']

    try:
        country_info = CountryInfo(code)
        population = country_info.population()
        area = country_info.area()
        if area is None or population is None:
            density = None
        else:
            try:
                density = area / population
            except ZeroDivisionError:
                density = 0.0

        # Aggiungi le informazioni su popolazione e densità alla riga corrispondente del DataFrame
        input_data.at[i, 'population'] = population
        input_data.at[i, 'urban_density'] = density

    except KeyError:
        print(f"Invalid ISO-2 code '{code}' for {country}. Skipping.")

# Scrivi il DataFrame aggiornato in un file di output
input_data.to_csv('countries_info.csv', index=False)


# Leggi i due file csv
df_codes = pd.read_csv('country_codes.csv')
df_info = pd.read_csv('paesi_info.csv')

# Seleziona solo le colonne desiderate dal dataframe df_info
input_data = input_data.loc[:, ['code', 'population', 'urban_density']]

# Esegui la left join sulla colonna code
df_merged = pd.merge(df_codes, input_data, on='code', how='left')

# Salva il risultato in un nuovo file csv
df_merged.to_csv('merged.csv', index=False)