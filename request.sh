#!/bin/bash

Key="bbefabce-4d0d-4a0c-af73-2ac6b0f1bd8f"

curl -H ${Key} 'https://api.airvisual.com/v2/countries?key=${Key}' > output.json
