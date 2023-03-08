#!/bin/bash

# Connessione al database PostgreSQL
PGHOST="localhost"
PGUSER="dlbd"
PGPASSWORD="admin2022"
PGDATABASE="master_db"
export PGPASSWORD

# Nome della tabella
TABLE_NAME="earthquake_data"

# File CSV di input
INPUT_CSV="earthquakes.csv"

# Creazione della tabella
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "
  CREATE TABLE IF NOT EXISTS public.$TABLE_NAME (
    Time date,
    Latitude double precision,
    Longitude double precision,
    Place text,
    Mag double precision
  );
"

# Inserimento dei dati dalla tabella CSV
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "\copy earthquake_data(Time, Latitude, Longitude, Place, Mag) FROM 'earthquakes.csv' WITH (FORMAT csv, HEADER true);"
