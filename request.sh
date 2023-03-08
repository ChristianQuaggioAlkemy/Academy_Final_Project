#!/bin/bash

#Key="bbefabce-4d0d-4a0c-af73-2ac6b0f1bd8f"
#Key="f1vgBXoJNyodq4eAlJBJ0Aq9qlXcmzspk4s0HUlQ"
#Key="Fx32e8_YNlY7mDRVxU2TdofdZnBYuFjD"
Key="0342d6f2dc0d423382717db8384e8f6d"

#curl "https://api.airvisual.com/v2/countries?key=${Key}" > output.json
#curl "http://api.airvisual.com/v2/country?country=Italy&key=${Key}" > output_Italy.json
#curl "http://api.airvisual.com/v2/cities?state=Lombardy&country=Italy&key=${Key}" > output_Lombardy.json
#curl "http://api.airvisual.com/v2/states?country=Italy&key=${Key}" > output_Italy.json
#curl "http://api.airvisual.com/v2/city?city=Milano&state=Lombardy&country=Italy&key=${Key}" > Milano.json
#curl "https://api.eia.gov/v2/coal/aggregate-production/data/?frequency=annual&data[0]=average-employees&data[1]=labor-hours&data[2]=number-of-mines&data[3]=production&data[4]=productivity&start=2001&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key=${Key}" > output.json
#curl "http://api.worldbank.org/v2/country/IT/indicator/AG.LND.FRST.K2?format=json&per_page=1000" > output.json
#curl "https://api.polygon.io/v2/aggs/ticker/SPX/range/10/day/2000-10-09/2023-02-17?adjusted=true&limit=10&apiKey=Fx32e8_YNlY7mDRVxU2TdofdZnBYuFjD" > output.json
#curl "https://api.polygon.io/v1/open-close/SPX/2023-03-07?adjusted=true&apiKey=Fx32e8_YNlY7mDRVxU2TdofdZnBYuFjD"
#curl "https://api.polygon.io/v1/open-close/^GSPC/2022-03-04?adjusted=true&apiKey=Fx32e8_YNlY7mDRVxU2TdofdZnBYuFjD"
curl "https://api.twelvedata.com/time_series?symbol=SPX&interval=1day&outputsize=5000&apikey=${Key}" > output.json
