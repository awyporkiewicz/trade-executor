#!/bin/bash

# Set default values if the environment variables are not set
SYMBOL=${SYMBOL:-bnbusdt}
EXCHANGE=${EXCHANGE:-bid}

# Run your application using the environment variables
poetry run python main.py -q "$QUANTITY" -p "$PRICE" -s "$SYMBOL" -e "$EXCHANGE"