# Trade Executor

[![test](https://github.com/awyporkiewicz/trade-executor/actions/workflows/action.yml/badge.svg)](https://github.com/awyporkiewicz/trade-executor/actions/workflows/action.yml)

## Table of Contents
* [Introduction](#introduction)
* [General info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)
* [Example](#example)
* [Ideas for Project Development](#ideas-for-project-development)
* [Links](#links)

## Introduction
When trading on exchanges, understanding the different order types is crucial. Two primary order types commonly used are market orders and limit orders. Let's explore their features and trade-offs.

A market order executes at the current market price, ensuring trade execution but offering little control over the price. A limit order allows you to specify the price, but there's a risk of not getting the entire order executed if the market moves too quickly.

## General info
A trade execution service is required to address this situation. It should generate market orders based on the available liquidity in the order book. The service will take an order size and price for an asset pair, consume the order book ticker stream to evaluate current liquidity, and store the trade info in a SQLite database.

## Technologies
The project utilizes the following technologies:
- Python 3.11
- Websockets: A library for building WebSocket servers and clients in Python. 
- SQLite: A lightweight, serverless database engine used to store trade information.

## Usage
To use the Trade Execution Service, run the **main.py** script with appropriate command-line arguments.

Command-line arguments:
- **-q** or **--quantity**: The order quantity (required). 
- **-p** or **--price**: The order price (required). 
- **-s** or **--symbol**: The asset pair symbol (default: `bnbusdt`, choices: `bnbusdt`, `ethusdt`, `btcusdt`, `ethbtc`). 
- **-e** or **--exchange**: The exchange type (default: `bid`, choices: `bid`, `ask`).

## Example

#### INPUT
```commandline
python main.py --quantity=200 --price=246.00
```

#### OUTPUT
SQLite database, `schema.sql` with trade information of how the order size was split at the end.
```plaintext
Trade accepted: (8557162238, 'BNBUSDT', '246.30000000', '89.73000000')
Trade accepted: (8557162239, 'BNBUSDT', '246.30000000', '89.73000000')
Trade accepted: (8557162245, 'BNBUSDT', '246.30000000', '20.54000000')
Transaction finished.
```

## Ideas for Project Development
* Develop notification systems to alert users about trade execution and market updates.
* Build portfolio management features, including tracking balances and trade history.
* Incorporate advanced order types such as stop-loss and take-profit orders for enhanced trading strategies.

## Links
* [Binance API](https://binance-docs.github.io/apidocs/spot/en/#general-info)
* [Websockets](https://websockets.readthedocs.io/en/stable/)