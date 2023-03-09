import pandas as pd
import pycountry

# Crea una lista di dizionari, ognuno dei quali contiene le informazioni su un paese
countries = [{'code': country.alpha_2, 'country': country.name} for country in pycountry.countries]

# Crea un dataframe pandas con i dati dei paesi
df = pd.DataFrame(countries, columns=['code', 'country'])

# Salva il dataframe come file CSV
df.to_csv('country_codes.csv', index=False)
