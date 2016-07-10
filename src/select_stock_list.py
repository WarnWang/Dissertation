#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project: Dissertation
# File name: select_stock_list
# Author: Mark Wang
# Date: 5/7/2016

stock_list = ['0001.HK', '0002.HK', '0003.HK', '0004.HK', '0005.HK', '0006.HK', '0011.HK', '0012.HK', '0014.HK',
              '0016.HK', '0017.HK', '0019.HK', '0023.HK', '0027.HK', '0028.HK', '0031.HK', '0033.HK', '0043.HK',
              '0047.HK', '0050.HK', '0064.HK', '0066.HK', '0069.HK', '0076.HK', '0077.HK', '0078.HK', '0083.HK',
              '0095.HK', '0096.HK', '0101.HK', '0108.HK', '0109.HK', '0116.HK', '0117.HK', '0119.HK', '0120.HK',
              '0121.HK', '0123.HK', '0143.HK', '0144.HK', '0148.HK', '0151.HK', '0152.HK', '0153.HK', '0156.HK',
              '0173.HK', '0178.HK', '0179.HK', '0184.HK', '0189.HK', '0191.HK', '0193.HK', '0195.HK', '0196.HK',
              '0206.HK', '0208.HK', '0209.HK', '0215.HK', '0218.HK', '0219.HK', '0220.HK', '0223.HK', '0228.HK',
              '0229.HK', '0233.HK', '0242.HK', '0248.HK', '0258.HK', '0263.HK', '0265.HK', '0266.HK', '0267.HK',
              '0268.HK', '0272.HK', '0279.HK', '0288.HK', '0290.HK', '0291.HK', '0293.HK', '0299.HK', '0303.HK',
              '0309.HK', '0311.HK', '0312.HK', '0318.HK', '0319.HK', '0320.HK', '0330.HK', '0331.HK', '0335.HK',
              '0337.HK', '0342.HK', '0352.HK', '0354.HK', '0356.HK', '0358.HK', '0362.HK', '0363.HK', '0368.HK',
              '0373.HK', '0374.HK', '0375.HK', '0381.HK', '0382.HK', '0388.HK', '0392.HK', '0405.HK', '0422.HK',
              '0423.HK', '0425.HK', '0428.HK', '0434.HK', '0435.HK', '0455.HK', '0459.HK', '0460.HK', '0464.HK',
              '0467.HK', '0468.HK', '0471.HK', '0475.HK', '0477.HK', '0480.HK', '0483.HK', '0484.HK', '0486.HK',
              '0488.HK', '0494.HK', '0509.HK', '0511.HK', '0521.HK', '0522.HK', '0527.HK', '0531.HK', '0532.HK',
              '0538.HK', '0542.HK', '0543.HK', '0546.HK', '0557.HK', '0558.HK', '0563.HK', '0565.HK', '0566.HK',
              '0573.HK', '0575.HK', '0577.HK', '0580.HK', '0581.HK', '0592.HK', '0596.HK', '0599.HK', '0606.HK',
              '0607.HK', '0609.HK', '0612.HK', '0617.HK', '0633.HK', '0639.HK', '0646.HK', '0647.HK', '0648.HK',
              '0653.HK', '0656.HK', '0658.HK', '0660.HK', '0661.HK', '0662.HK', '0666.HK', '0682.HK', '0688.HK',
              '0690.HK', '0691.HK', '0695.HK', '0698.HK', '0699.HK', '0700.HK', '0709.HK', '0713.HK', '0732.HK',
              '0733.HK', '0737.HK', '0743.HK', '0745.HK', '0751.HK', '0752.HK', '0756.HK', '0762.HK', '0768.HK',
              '0769.HK', '0775.HK', '0776.HK', '0777.HK', '0799.HK', '0800.HK', '0801.HK', '0805.HK', '0806.HK',
              '0808.HK', '0813.HK', '0817.HK', '0819.HK', '0826.HK', '0828.HK', '0829.HK', '0832.HK', '0833.HK',
              '0836.HK', '0845.HK', '0846.HK', '0848.HK', '0850.HK', '0853.HK', '0856.HK', '0860.HK', '0862.HK',
              '0866.HK', '0868.HK', '0871.HK', '0872.HK', '0877.HK', '0880.HK', '0881.HK', '0882.HK', '0883.HK',
              '0884.HK', '0885.HK', '0886.HK', '0893.HK', '0905.HK', '0911.HK', '0923.HK', '0926.HK', '0928.HK',
              '0929.HK', '0930.HK', '0935.HK', '0936.HK', '0941.HK', '0951.HK', '0960.HK', '0963.HK', '0966.HK',
              '0973.HK', '0976.HK', '0978.HK', '0981.HK', '0992.HK', '1002.HK', '1006.HK', '1010.HK', '1022.HK',
              '1023.HK', '1029.HK', '1039.HK', '1043.HK', '1044.HK', '1051.HK', '1059.HK', '1062.HK', '1068.HK',
              '1070.HK', '1080.HK', '1083.HK', '1090.HK', '1094.HK', '1101.HK', '1102.HK', '1109.HK', '1110.HK',
              '1111.HK', '1112.HK', '1113.HK', '1114.HK', '1115.HK', '1116.HK', '1117.HK', '1125.HK', '1128.HK',
              '1142.HK', '1143.HK', '1148.HK', '1149.HK', '1150.HK', '1161.HK', '1164.HK', '1165.HK', '1169.HK',
              '1172.HK', '1174.HK', '1175.HK', '1177.HK', '1178.HK', '1180.HK', '1181.HK', '1193.HK', '1194.HK',
              '1195.HK', '1198.HK', '1210.HK', '1211.HK', '1212.HK', '1217.HK', '1219.HK', '1222.HK', '1228.HK',
              '1230.HK', '1232.HK', '1234.HK', '1238.HK', '1240.HK', '1245.HK', '1249.HK', '1250.HK', '1251.HK',
              '1252.HK', '1253.HK', '1255.HK', '1280.HK', '1293.HK', '1297.HK', '1299.HK', '1301.HK', '1305.HK',
              '1308.HK', '1313.HK', '1314.HK', '1317.HK', '1321.HK', '1326.HK', '1329.HK', '1333.HK', '1335.HK',
              '1338.HK', '1345.HK', '1348.HK', '1358.HK', '1360.HK', '1361.HK', '1368.HK', '1370.HK', '1373.HK',
              '1378.HK', '1381.HK', '1383.HK', '1386.HK', '1388.HK', '1390.HK', '1393.HK', '1396.HK', '1418.HK',
              '1431.HK', '1432.HK', '1438.HK', '1450.HK', '1478.HK', '1515.HK', '1530.HK', '1548.HK', '1555.HK',
              '1600.HK', '1613.HK', '1616.HK', '1619.HK', '1622.HK', '1623.HK', '1628.HK', '1638.HK', '1661.HK',
              '1678.HK', '1680.HK', '1685.HK', '1689.HK', '1700.HK', '1728.HK', '1733.HK', '1778.HK', '1788.HK',
              '1808.HK', '1811.HK', '1813.HK', '1828.HK', '1830.HK', '1831.HK', '1833.HK', '1836.HK', '1862.HK',
              '1880.HK', '1882.HK', '1883.HK', '1886.HK', '1888.HK', '1889.HK', '1899.HK', '1908.HK', '1910.HK',
              '1918.HK', '1928.HK', '1929.HK', '1966.HK', '1968.HK', '1991.HK', '1998.HK', '2005.HK', '2007.HK',
              '2008.HK', '2012.HK', '2014.HK', '2018.HK', '2020.HK', '2038.HK', '2080.HK', '2083.HK', '2098.HK',
              '2100.HK', '2128.HK', '2168.HK', '2178.HK', '2183.HK', '2198.HK', '2200.HK', '2211.HK', '2226.HK',
              '2228.HK', '2233.HK', '2236.HK', '2268.HK', '2280.HK', '2282.HK', '2298.HK', '2299.HK', '2300.HK',
              '2302.HK', '2303.HK', '2307.HK', '2309.HK', '2312.HK', '2314.HK', '2317.HK', '2331.HK', '2336.HK',
              '2339.HK', '2342.HK', '2348.HK', '2349.HK', '2356.HK', '2358.HK', '2362.HK', '2368.HK', '2369.HK',
              '2371.HK', '2382.HK', '2383.HK', '2388.HK', '2389.HK', '2398.HK', '2608.HK', '2662.HK', '2669.HK',
              '2678.HK', '2689.HK', '2700.HK', '2728.HK', '2788.HK', '2789.HK', '2822.HK', '2877.HK', '2878.HK',
              '2888.HK', '2903.HK', '2910.HK', '2921.HK', '2960.HK', '2988.HK', '3009.HK', '3019.HK', '3027.HK',
              '3035.HK', '3085.HK', '3308.HK', '3311.HK', '3313.HK', '3318.HK', '3331.HK', '3333.HK', '3335.HK',
              '3336.HK', '3337.HK', '3339.HK', '3366.HK', '3368.HK', '3377.HK', '3382.HK', '3383.HK', '3386.HK',
              '3389.HK', '3393.HK', '3398.HK', '3633.HK', '3639.HK', '3668.HK', '3669.HK', '3683.HK', '3709.HK',
              '3777.HK', '3788.HK', '3800.HK', '3818.HK', '3828.HK', '3836.HK', '3838.HK', '3883.HK', '3888.HK',
              '3889.HK', '3899.HK', '3900.HK', '3918.HK', '3933.HK', '3988.HK', '3998.HK', '6136.HK', '6139.HK',
              '6166.HK', '6210.HK', '6230.HK', '6808.HK', '6823.HK', '6836.HK', '6863.HK', '6882.HK', '6893.HK',
              '6899.HK', '8001.HK', '8002.HK', '8006.HK', '8008.HK', '8025.HK', '8029.HK', '8032.HK', '8036.HK',
              '8041.HK', '8050.HK', '8056.HK', '8061.HK', '8071.HK', '8092.HK', '8103.HK', '8116.HK', '8117.HK',
              '8122.HK', '8123.HK', '8129.HK', '8132.HK', '8137.HK', '8138.HK', '8140.HK', '8156.HK', '8163.HK',
              '8171.HK', '8176.HK', '8186.HK', '8190.HK', '8195.HK', '8198.HK', '8201.HK', '8202.HK', '8203.HK',
              '8206.HK', '8218.HK', '8219.HK', '8220.HK', '8226.HK', '8242.HK', '8250.HK', '8255.HK', '8256.HK',
              '8260.HK', '8267.HK', '8268.HK', '8279.HK', '8315.HK', '8317.HK', '8320.HK', '8325.HK', '8326.HK']

predict_list = ['0001.HK', '0002.HK', '0003.HK', '0004.HK', '0005.HK', '0006.HK', '0008.HK', '0009.HK', '0010.HK',
                '0011.HK', '0012.HK', '0013.HK', '0014.HK', '0015.HK', '0016.HK', '0017.HK', '0018.HK', '0019.HK',
                '0020.HK', '0023.HK', '0024.HK', '0025.HK', '0027.HK', '0031.HK', '0032.HK', '0034.HK', '0035.HK',
                '0038.HK', '0039.HK', '0041.HK', '0042.HK', '0043.HK', '0044.HK', '0045.HK', '0052.HK', '0053.HK',
                '0054.HK', '0056.HK', '0057.HK', '0062.HK', '0064.HK', '0065.HK', '0066.HK', '0088.HK', '0168.HK',
                '0688.HK', '0700.HK', '0888.HK', '1123.HK', '6823.HK']

predict_list2 = ['0001.HK', '0002.HK', '0003.HK', '0004.HK', '0005.HK', '0006.HK', '0011.HK', '0012.HK', '0014.HK',
                 '0016.HK', '0017.HK', '0019.HK', '0023.HK', '0027.HK', '0031.HK', '0043.HK', '0064.HK', '0066.HK',
                 '0120.HK', '0268.HK', '0291.HK', '0455.HK', '0471.HK', '0546.HK', '0577.HK', '0688.HK', '0700.HK',
                 '0737.HK', '0745.HK', '0777.HK', '0845.HK', '0872.HK', '1051.HK', '1112.HK', '1117.HK', '1181.HK',
                 '1230.HK', '1251.HK', '1314.HK', '1361.HK', '1613.HK', '1918.HK', '2005.HK', '2362.HK', '2383.HK',
                 '2789.HK', '3777.HK', '6823.HK', '8050.HK', '8123.HK']

predict_list3 = ['0001.HK', '0002.HK', '0003.HK', '0004.HK', '0005.HK', '0006.HK', '0011.HK', '0012.HK', '0014.HK',
                 '0016.HK', '0017.HK', '0019.HK', '0023.HK', '0027.HK', '0031.HK', '0043.HK', '0064.HK', '0066.HK',
                 '0233.HK', '0267.HK', '0268.HK', '0291.HK', '0455.HK', '0546.HK', '0633.HK', '0688.HK', '0700.HK',
                 '0733.HK', '0737.HK', '0777.HK', '0845.HK', '0886.HK', '0929.HK', '0976.HK', '1044.HK', '1051.HK',
                 '1068.HK', '1110.HK', '1169.HK', '1195.HK', '1313.HK', '1361.HK', '1386.HK', '1918.HK', '2005.HK',
                 '2168.HK', '2362.HK', '2383.HK', '3331.HK', '6823.HK']