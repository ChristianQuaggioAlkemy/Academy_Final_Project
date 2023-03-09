# Creazione di un database contenente informazioni su terremoti e valori azionari
Questo progetto fornisce uno script di shell per creare un database contenente informazioni su terremoti e valori azionari. L'obiettivo principale del progetto è fornire un database completo e integrato per l'analisi di dati relativi a terremoti e valori azionari.

## Utilizzo

Eseguire lo script step_1_collect_data.sh per integrare i dati contenuti in earthquakes.csv con diverse API.
```
./step_1_collect_data.sh <stock_code> <date (YYYY-MM-DD)>
```
Dove <stock_code> è il codice identificativo del titolo azionario e <date> è la data di riferimento nel formato YYYY-MM-DD. 
Questo script eseguirà diverse chiamate alle API per arricchire i dati sul terremoto con altre informazioni, come il luogo di origine e informazioni demografiche. Verranno raccolti anche i dati relativi al valore di chiusura dell'azione scelta per ogni giorno dalla data scelta. I dati verranno salvati in tre file csv: earthquakes_data, countries_info e index_stocks_data.

Creare un database su postgres e popolarlo con le informazioni raccolte utilizzando lo script step_2_load_psql.sh.
```
./step_2_load_psql.sh
```
Questo script creerà diverse tabelle all'interno del database master_db per archiviare i dati raccolti. Successivamente, verrà eseguito il caricamento dei dati dai file earthquakes_data, countries_info e index_stocks_data nelle rispettive tabelle del database.
