#!/bin/bash

# Connessione al database PostgreSQL
PGHOST="localhost"
PGUSER="dlbd"
PGPASSWORD="admin2022"
PGDATABASE="master_db"
export PGPASSWORD

# Nome delle tabelle
TABLE_EQ="earthquake_data"
TABLE_CC="countries_info"
TABLE_ISD="index_stock_data"

# File CSV di input
INPUT_EQ="earthquakes_data.csv"
INPUT_CC="countries_info.csv"
INPUT_ISD="index_stocks_data.csv"

# Creazione della tabella earthquake_data
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "
  CREATE TABLE IF NOT EXISTS public.$TABLE_EQ (
    Data date PRIMARY KEY,
    Location text,
    Country char(2),
    Latitude double precision,
    Longitude double precision,
    Depth double precision,
    Mag double precision,
    MagType varchar(5)
  );"

# Popolamento della tabella earthquake_data
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "\copy $TABLE_EQ(Data, Location, Country, Latitude, Longitude, Depth, Mag, MagType) FROM '$INPUT_EQ' WITH (FORMAT csv, HEADER true);"

# Creazione della tabella countries_info
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "
  CREATE TABLE IF NOT EXISTS public.$TABLE_CC (
    Code char(2) PRIMARY KEY,
    Country text,
    Population numeric,
    UrbanDensity numeric
  );"

# Popolamento della tabella countries_info
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "\copy $TABLE_CC(Code, Country, Population, UrbanDensity) FROM '$INPUT_CC' WITH (FORMAT csv, HEADER true);"

# Creazione della tabella index_stock_data
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "
  CREATE TABLE IF NOT EXISTS public.$TABLE_ISD (
    Data date PRIMARY KEY,
    AdjClose numeric
  );"

# Popolamento della tabella index_stock_data
psql -h $PGHOST -U $PGUSER -d $PGDATABASE -c "\copy $TABLE_ISD(Data, AdjClose) FROM '$INPUT_ISD' WITH (FORMAT csv, HEADER true);"
