#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project: Dissertation
# File name: stock_prediction
# Author: Mark Wang
# Date: 13/6/2016

import os
import sys
import time

from StockInference.inference_system import InferenceSystem
from StockInference.util.data_parse import *
from StockInference.constant import Constants

const = Constants()

required_info = {
    const.PRICE_TYPE: const.STOCK_CLOSE,
    const.STOCK_PRICE: {const.DATA_PERIOD: 5},
    const.STOCK_INDICATOR: [
        (const.MACD, {
            const.MACD_FAST_PERIOD: 12,
            const.MACD_SLOW_PERIOD: 26,
            const.MACD_TIME_PERIOD: 9
        }),
        (const.MACD, {
            const.MACD_FAST_PERIOD: 7,
            const.MACD_SLOW_PERIOD: 14,
            const.MACD_TIME_PERIOD: 9
        }),
        (const.SMA, 3),
        (const.SMA, 13),
        (const.SMA, 21),
        (const.EMA, 5),
        (const.EMA, 13),
        (const.EMA, 21),
        (const.ROC, 13),
        (const.ROC, 21),
        (const.RSI, 9),
        (const.RSI, 14),
        (const.RSI, 21),
    ],
    const.FUNDAMENTAL_ANALYSIS: [
        # const.US10Y_BOND,
        # const.US30Y_BOND,
        const.FXI,
        const.IC,
        const.IA, # comment this  two because this two bond is a little newer
        const.HSI,
        {const.FROM: const.USD, const.TO: const.HKD},
        {const.FROM: const.EUR, const.TO: const.HKD},
        # {const.FROM: const.AUD, const.TO: const.HKD},
        const.ONE_YEAR,
        const.HALF_YEAR,
        # const.OVER_NIGHT,
        # const.GOLDEN_PRICE,
        const.SHSE,
    ]
}

output_path = 'output'
data_path = 'data'
model_path = "models"

if sys.platform == 'darwin':
    output_path = '../{}'.format(output_path)
    data_path = '../{}'.format(data_path)
    model_path = '../{}'.format(model_path)

if not os.path.isdir(data_path):
    os.makedirs(data_path)
stock_list = ['0001.HK', '0002.HK', '0003.HK', '0004.HK', '0005.HK', '0006.HK', '0007.HK', '0008.HK', '0009.HK',
              '0010.HK', '0011.HK', '0012.HK', '0013.HK', '0014.HK', '0015.HK', '0016.HK', '0017.HK', '0018.HK',
              '0019.HK', '0020.HK', '0021.HK', '0022.HK', '0023.HK', '0024.HK', '0025.HK', '0026.HK', '0027.HK',
              '0028.HK', '0029.HK', '0030.HK', '0031.HK', '0032.HK', '0700.HK', '0034.HK', '0035.HK', '0036.HK',
              '0068.HK', '0038.HK', '0039.HK', '0040.HK', '0041.HK', '0042.HK', '0043.HK', '0044.HK', '0045.HK',
              '0046.HK', '0088.HK', '0050.HK', '0051.HK', '0052.HK', '0053.HK', '0054.HK', '0168.HK', '0056.HK',
              '0057.HK', '0058.HK', '0059.HK', '0060.HK', '0888.HK', '0062.HK', '0063.HK', '0064.HK', '0065.HK',
              '0066.HK', '1123.HK']

test = None
for method in [const.ARTIFICIAL_NEURAL_NETWORK, const.RANDOM_FOREST, const.LINEAR_REGRESSION]:

    new_file_path = os.path.join(output_path, method)
    if not os.path.isdir(new_file_path):
        os.makedirs(new_file_path)

    f = open(os.path.join(new_file_path, "stock_info.csv"), 'w')
    f.write('stock,MSE,MAPE,MAD,RMSE,CDC\n')
    for stock in stock_list[:10]:

        specific_file_path = os.path.join(new_file_path, stock[:4])
        specific_model_path = os.path.join(model_path, method, stock[:4])
        test = InferenceSystem(stock, training_method=method, data_folder_path=data_path, using_exist_model=False,
                               output_file_path=specific_file_path, model_path=specific_model_path)
        try:
            predict_result = test.predict_historical_data(0.75, "2010-12-29", "2015-01-06", iterations=10)
            predict_result.cache()
            mse = get_MSE(predict_result)
            mape = get_MAPE(predict_result)
            mad = get_MAD(predict_result)
            rmse = get_RMSE(predict_result)
            # tie = get_theils_inequality_coefficient(predict_result)
            cdc = get_CDC(predict_result)
            f.write('{},{},{},{},{},{}\n'.format(stock, mse, mape, mad, rmse, cdc))
        except Exception, err:
            print "Error happens"
            print err
            time.sleep(20)

    f.close()

if hasattr(test, 'sc'):
    test.sc.stop()

