#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project: Dissertation
# File name: plot_data
# Author: Mark Wang
# Date: 25/4/2016

import numpy as np

symbol_list = ['r-', 'b-', 'y-', 'm-', 'g-', 'c-', 'k-']
colors = ['r', 'b', 'y', 'm', 'g', 'c', 'k']


def plot_predict_and_real(data, graph_index=0, graph_title=None, plt=None):
    return plot_label_vs_data(data, ["Predict Price", "Real Price"], graph_index=graph_index,
                              graph_title=graph_title, plt=plt)


def plot_label_vs_data(data, label, graph_index=0, graph_title=None, plt=None):
    if plt is None:
        import matplotlib.pyplot as plt
    plt.figure(graph_index)
    plt.title(graph_title)
    plt.ylabel("Stock Price")
    plt.xlabel("Date")
    data = np.array(data)
    data = data.T
    plt_list = []
    for i in range(len(data)):
        plt_list.append(plt.plot(data[i], symbol_list[i])[0])
    plt.legend(plt_list, label, loc=1)
    return plt


def plot_bar(data, legend, x_axis=None, y_label="Price", x_label="Days", graph_index=0, graph_title='None', plt=None):
    if plt is None:
        import matplotlib.pyplot as plt

    # plt.figure(graph_index)
    ind = np.arange(len(data[0]))
    width = 0.35

    fig, ax = plt.subplots()
    rects = []
    ax.set_title(graph_title)
    ax.set_xticks(ind + width)
    if x_axis is not None:
        ax.set_xticklabels(x_axis)

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    for i, j in enumerate(data):
        print i, j
        rects.append(ax.bar(ind + width * i, j, width, color=colors[i]))
    ax.legend(rects, legend, loc=2)
    return plt

def plot_data():
    inf = 'inf'
    non_normalize_mse = [4.2099151573371971, 0.47288044013021874, 2.8130426897877965, 1.1467855762895549,
                         1.2275066999971787, 1.3203662766607924, 1.0966251179360333, 21.594347564159801,
                         1.0632430284143002, 0.5773589752260514, 4.6010440233875798, 1.3845958953188289,
                         3.3223536435851782, 1.9934631090193389, 0.34135239878659451, 3.6222139404609686,
                         7.7803972749409951, 0.76189933298765011, 2.1500600712913296, 3.1142486857009155,
                         0.068181177560338174, 0.091012563244407527, 0.6235839916910243, 0.10043998121035125,
                         56.360561406893012, 2.6196573383898127, 5.794108572663232, 19.280291805997656,
                         9.8200850605981955, 0.039227449950666703, 1.2813820712554587, 46.162061997300569,
                         0.024460160329826661, 11.490377354159421, 8.8862929597429829, 2.2089943224440667,
                         0.24072227294812595, 23.709269084678539, 4.7653219125491777, 0.75424542119456417,
                         2.6728240841852586, 5.1271578205059356, 0.81117502039424327, 0.73390416996375596,
                         15.579038947850558, 7.6854989992935758, 0.13152056587302358, 46.475248427222148,
                         24.269385650283784, 67.989772062512088, 0.58682805443063424, 1.5461992563840581,
                         0.0011659811147937279, 2.4992938518010317, 4.0930534390932642, 0.1444658226352184,
                         0.59312945973022524, 1.2183915232133338, 0.00022493561184761644, 0.58245921158791136,
                         0.25212881498580486, 0.12325760417174493, 0.25746125499809236]

    non_normalize_mape = [0.014715366858634914, 0.0082154588202181487, 0.091265205662109314, 0.017184484706964959,
                          0.012581095857833876, 0.01221711163257125, 0.99825540688140602, 0.97942308482771534,
                          0.99973311941147469, 0.01715806098686052, 0.010909894422736028, 0.016504648916662472,
                          0.013321265673457712, 0.037551979284252163, 0.9997194391589419, 0.013233185796378262,
                          0.31596578775732898, 0.99922031897384478, 0.011939887721068238, 0.042670974449278698,
                          0.99986478091384834, 0.99995733561904965, 0.021827313692162169, 0.99977530825728789,
                          0.56340563830005452, 0.012917963490223942, 0.050428096519084718, 0.89852192876572323,
                          0.99664684489488398, 0.99915614265424835, 0.99942789046150349, 0.78928363393896339,
                          0.99883901340909576, 0.37905082927985223, 0.99586395330578603, 0.9994065358861689,
                          0.9999621284518726, 0.89453607318818729, 0.99806582521804066, 0.99943292624447444,
                          0.058963230738984955, 0.99870203539870805, 0.99972038738929903, 0.0089822174878562283,
                          0.38089154278146908, 0.99850781969900504, 0.99979029384221396, 0.7408053700749101,
                          0.36256160600386811, 0.39640721740709961, 0.0061890081181753794, 0.043109735129581772,
                          0.99999971385421904, 0.98594195155254305, 0.98268792708916686, 0.99995267788287356,
                          0.99937411802018572, 0.99926617061886325, inf, 0.039397365779482302, 0.99995390475979662,
                          0.99984450768352484, 0.99998316141498289]

    non_normalize_mad = [1.5222193132824153, 0.54311438520546174, 1.6445521314653002, 0.8641466709802913,
                         0.83358232285356548, 0.87496184545758016, 1.0110316258160672, 4.6321250368112743,
                         0.92620197242720814, 0.5866542080960504, 1.5155597760912118, 0.88325572448175882,
                         1.3505573687040742, 1.3044932508068969, 0.57928737246479389, 1.4324870346048848,
                         2.7629640319695636, 0.87089746859569583, 1.1109038683961374, 1.5805420334188935,
                         0.25546978717308189, 0.29375090686878019, 0.66157615747582621, 0.31214920864492818,
                         7.4845595392245663, 1.047628658427062, 1.9815885529168824, 4.3529923795893781,
                         3.1158094639611349, 0.18251260282401108, 1.0907687019844083, 6.6964158350037168,
                         0.14913219554770016, 3.3640712572638716, 2.9575701596785962, 1.1318704340685937,
                         0.45359563374500034, 4.806993141171338, 1.74869267603909, 0.85887597164070195,
                         1.5697043464561855, 2.1914116691421857, 0.88849275955376283, 0.64065602995703397,
                         3.902841194968421, 2.752161000608083, 0.34213342192213453, 6.7590512730633883,
                         4.9221092991717574, 8.1527017642558892, 0.55276987139654243, 1.1859575927042134,
                         0.019777772190828411, 1.5609579407875038, 2.0090575022438752, 0.3555031092926545,
                         0.76018841769385703, 1.0925318007397116, 0.0079108905287249738, 0.71478826783115634,
                         0.42986908062239942, 0.3462109451766523, 0.44519213149955189]

    normalize_mse = [4.0266251940717703, 0.47953679474108507, 0.084029394785497702, 1.0672657721696304,
                     1.1961563368079096, 1.3459160287808376, 0.0022456419628239452, 0.0076311994324478631,
                     0.0068026558398070125, 0.49526461769717267, 4.583344958156883, 1.3623955613044065,
                     3.2287331191390485, 0.3210721707134393, 0.00033774078502716963, 3.6460927548262267,
                     0.02892111668240601, 0.00035879401212627205, 2.1838488286795044, 0.60614218386368579,
                     0.00025510645712246603, 0.00028462153122057305, 0.30119203231378888, 0.00031199043476615981,
                     0.042468087298319558, 2.4183605251102627, 2.1188754527363662, 0.0077234902437333212,
                     0.011910670552949818, 0.00024454301186909442, 0.0036299192127679661, 0.021678477671415817,
                     0.00013180527682506073, 0.021225776417766424, 0.0062812334814230939, 0.033730819975738513,
                     0.0018001884648862836, 0.045209746227138518, 0.059714704681845178, 0.00088899356543944378,
                     0.19259952644043277, 0.013346641848088977, 0.0011660798856103676, 0.73609748109756779,
                     0.029046519976520208, 0.006464764097115494, 0.0011101427119566622, 0.042661568686946399,
                     0.025601219323275935, 0.10020364252017679, 0.56024007703555068, 0.14484532517922419,
                     0.0011694630909134447, 0.0024499114398419432, 0.0012475004084774575, 0.00091018623660251504,
                     0.00174775305166872, 0.0016890041627079433, 6.6943068760474249e-06, 0.070621208927338391,
                     0.0017444092140124806, 0.00020609002479564319, 0.0018610591184837378]

    normalize_mape = [0.014616150755712116, 0.0083207318365260876, 0.011652154684554737, 0.017021541125803751,
                      0.01261801510507308, 0.012447106213443686, 0.033120157513785317, 0.013893290713219535,
                      0.037503276884488859, 0.016094702181725547, 0.011089987305268221, 0.016527580397299742,
                      0.013314397588644824, 0.012592167148162695, 0.021157508755866087, 0.013456177746404639,
                      0.015066640269620919, 0.01263625791714613, 0.012210325786553676, 0.016692223267271142,
                      0.042497716080881577, 0.032160296354674024, 0.014326406371994702, 0.035399858968109585,
                      0.010240804020946846, 0.013168945284383936, 0.030041833806897136, 0.013466304142013059,
                      0.023847626267317078, 0.041835469508710539, 0.031347260110433837, 0.011345570661247173,
                      0.046962805962198338, 0.012144161439959849, 0.018744229478108942, 0.053994241295690096,
                      0.045349384971192418, 0.026588314889666381, 0.053561506515365342, 0.023188415751141729,
                      0.012579530507278461, 0.034388262223354372, 0.0229357802395549, 0.0093412887599597615,
                      0.012841434665408371, 0.017448264396937817, 0.04551767306210152, 0.013129379121888012,
                      0.0082078516319933435, 0.01086330522244942, 0.0061792926989715589, 0.011010183391991911,
                      0.099996931892434138, 0.018723893874478315, 0.012849251366853958, 0.046817737270160031,
                      0.033350493331709127, 0.024732942157047043, inf, 0.009938100385481834, 0.048931931268235078,
                      0.025313779649496267, 0.047606010072150685]

    normalize_mad = [1.5127119268720837, 0.54973877566688778, 0.20599221216304028, 0.84885347378616527,
                     0.8373466034993049, 0.89089577610603587, 0.032091559249222745, 0.065096272614965242,
                     0.042321601889288851, 0.53799559111201667, 1.5410555929089618, 0.88581890917432049,
                     1.3500778077458853, 0.4309527480199391, 0.012548263286982244, 1.4595042199062618,
                     0.12902139870227408, 0.01108653148803718, 1.138910950206, 0.61472564234816918,
                     0.011066984136895226, 0.010119274024516574, 0.42308114323002882, 0.011406742399167185,
                     0.13702518294193433, 1.0644825583631563, 1.1365688363628059, 0.062501476408215573,
                     0.074831087869571433, 0.0085757245300679321, 0.036343073137021495, 0.1003136180211442,
                     0.0073356745489453739, 0.10402557624453902, 0.056519264972127503, 0.059861955386998511,
                     0.023214129413598687, 0.14402057412320435, 0.10306361502999437, 0.020540521355514783,
                     0.33242024851344104, 0.075158476168407734, 0.020967083183841592, 0.6685352105803688,
                     0.12706731598358956, 0.050660990001827749, 0.018095318474346693, 0.12538712974750038,
                     0.1110151454601427, 0.22970049223486605, 0.55236039717921503, 0.2970031757529138,
                     0.0046863417412026497, 0.031660339891845586, 0.026084606669603782, 0.017494101423509628,
                     0.026327350098070194, 0.027623279506449685, 0.0008490098941977308, 0.1828031005851318,
                     0.023620052306820256, 0.0089763089377997221, 0.021636251867698998]

    label = ['0001.HK.csv', '0002.HK.csv', '0003.HK.csv', '0004.HK.csv', '0005.HK.csv', '0006.HK.csv', '0007.HK.csv',
             '0008.HK.csv', '0009.HK.csv', '0010.HK.csv', '0011.HK.csv', '0012.HK.csv', '0013.HK.csv', '0014.HK.csv',
             '0015.HK.csv', '0016.HK.csv', '0017.HK.csv', '0018.HK.csv', '0019.HK.csv', '0020.HK.csv', '0021.HK.csv',
             '0022.HK.csv', '0023.HK.csv', '0024.HK.csv', '0025.HK.csv', '0026.HK.csv', '0027.HK.csv', '0028.HK.csv',
             '0029.HK.csv', '0030.HK.csv', '0031.HK.csv', '0032.HK.csv', '0033.HK.csv', '0034.HK.csv', '0035.HK.csv',
             '0036.HK.csv', '0037.HK.csv', '0038.HK.csv', '0039.HK.csv', '0040.HK.csv', '0041.HK.csv', '0042.HK.csv',
             '0043.HK.csv', '0044.HK.csv', '0045.HK.csv', '0046.HK.csv', '0048.HK.csv', '0050.HK.csv', '0051.HK.csv',
             '0052.HK.csv', '0053.HK.csv', '0054.HK.csv', '0055.HK.csv', '0056.HK.csv', '0057.HK.csv', '0058.HK.csv',
             '0059.HK.csv', '0060.HK.csv', '0061.HK.csv', '0062.HK.csv', '0063.HK.csv', '0064.HK.csv', '0065.HK.csv']

    data = [label, non_normalize_mad, non_normalize_mape, non_normalize_mse,
            normalize_mad, normalize_mape, normalize_mse]

    import numpy as np
    array = np.array(data).T
    f = open('error_data.csv', "w")
    f.write(
        "symbol,Non-Normalized MAD,Non-Normalized MAPE,Non-Normalized MSE,Normalized MAD,Normalized MAPE,Normalized MSE\n")
    for i in array:
        if float(i[1]) < 3 and float(i[2]) < 0.1 and float(i[3]) < 6:
            f.write('{}\n'.format(','.join(i)))

    f.close()


if __name__ == "__main__":
    plot_data()