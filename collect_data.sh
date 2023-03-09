#!/bin/bash

# Verifica che siano stati passati i parametri corretti
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <stock_code> <date>"
    exit 1
fi

# Assegna i parametri a delle variabili
STOCK_CODE=$1
DATE=$2

# Esegue lo script dataset_eq.py con la data in input
python3 dataset_eq.py $DATE

# Esegue lo script stocks_data_new.py con il codice azionario e la data in input
python3 stocks_data_new.py $STOCK_CODE $DATE

# Esegue lo script country_codes.py
python3 country_codes.py

# Esegue lo script demographic_info.py
python3 demographic_info.py