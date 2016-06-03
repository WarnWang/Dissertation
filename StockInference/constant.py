#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project: Dissertation
# File name: constant
# Author: Mark Wang
# Date: 30/5/2016


class Constants(object):

    # information used in stock price info
    STOCK_PRICE = "history_price"
    STOCK_HIGH = "stock_high"
    STOCK_LOW = "stock_low"
    STOCK_OPEN = "stock_open"
    STOCK_CLOSE = "stock_close"
    DATA_PERIOD = "data_period"

    # information for indicators info
    STOCK_INDICATOR = "indicator"

    # For macd info
    MACD = "MACD"
    MACD_SLOW_PERIOD = "MACD slow period"
    MACD_FAST_PERIOD = "MACD fast period"
    MACD_TIME_PERIOD = "MACD time period"

    # For moving average info
    SMA = "simple moving average"
    EMA = "Exponential moving average"
    ROC = "Rate of change"
    RSI = "Relative strength index"

    # Fundamental Analysis
    FUNDAMENTAL_ANALYSIS = "fundamental analysis"

    # Bond, index and ETF related
    US10Y_BOND = "CBOE Interest Rate 10 Year T No" # Symbol ^TNX
    US30Y_BOND = "Treasury Yield 30 Years" # Symbol ^TYX
    HSI = "Hang Seng Index" # ^HSI
    FXI = "iShares China Large-Cap"
    IC = "2801.HK" # iShares China
    IA = "iShares CSI A-Share Financials" # 2829.HK
    IA300 = "iShares CSI 300 A-Share" # 2846.HK
    IMSCI = "iShares MSCI AC Asia ex Japan" # 3010.HK

    # Normalization method
    MIN_MAX = "Min-Max Normalization"
    SIGMOID = "Sigmoid Normalization"

    # define constants used in get loss function
    LSE = 'least square error'
    LAE = 'least absolute error'

    # define method type used in neural network regression type
    BP_SGD = 'back propagation with stochastic gradient descent'
    BP = 'back propagation'

    # define method used in linear regression
    GD = 'Standard gradient descent'