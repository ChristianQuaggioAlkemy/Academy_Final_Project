#!/bin/bash

# Connessione al database PostgreSQL
PGHOST="db"
PGPORT="5432"
PGUSER="dlbd"
PGPASSWORD="admin2022"
PGDATABASE="master_db"
export PGPASSWORD

# Nome della tabella
TABLE_NAME="earthquake_data"

# File CSV di input
INPUT_CSV="earthquake.csv"

# Creazione della tabella
psql -h $PGHOST -p $PGPORT -U $PGUSER -d $PGDATABASE -c "
  CREATE TABLE IF NOT EXISTS public.$TABLE_NAME (
    time timestamp with time zone,
    latitude double precision,
    longitude double precision,
    depth double precision,
    magnitude double precision,
    magtype text,
    mb double precision,
    ms double precision,
    mww double precision,
    place text
  );
"

# Inserimento dei dati dalla tabella CSV
psql -h $PGHOST -p $PGPORT -U $PGUSER -d $PGDATABASE -c "
  COPY public.$TABLE_NAME(time, latitude, longitude, depth, magnitude, magtype, mb, ms, mww, place)
  FROM '$INPUT_CSV'
  DELIMITER ','
  CSV HEADER;
"

