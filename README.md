# Trade Executor

[![test](https://github.com/awyporkiewicz/trade-executor/actions/workflows/poetry_action.yml/badge.svg)](https://github.com/awyporkiewicz/trade-executor/actions/workflows/poetry_action.yml)


## Table of Contents
* [Introduction](#introduction)
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Usage](#usage)
* [Links](#links)


## Introduction
When trading on exchanges, understanding the different order types is crucial. Two primary order types commonly used are market orders and limit orders. Let's explore their features and trade-offs.
- **A market order** executes at the current market price, ensuring trade execution but offering little control over the price. 
- **A limit order** allows you to specify the price, but there's a risk of not getting the entire order executed if the market moves too quickly.

## General info
A trade execution service is required to address this situation. 
It should generate market orders **based on the available liquidity** in the order book. 
The service will take an **order size and price** for an asset pair, consume the order book ticker stream to evaluate current liquidity. 
It will store the trade info in a SQLite database, a little summary how the order size was split at the end.


## Technologies
Project is created with:
* Python: 3.11

## Features
...

## Usage
...

**INPUT**
```
...
```

**OUTPUT_1**
```
...
```

## Links
...