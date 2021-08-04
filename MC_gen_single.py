import matplotlib.pyplot as plt
import pandas as pd
import random
# from tqdm import tqdm

def runMCSingle(settings):
    simulationsCount = settings['simulationsCount']
    randomCurves = settings['randomCurves']
    tradesCount = settings['tradesCount']
    winRate = settings['winRate']
    winLosRatio = settings['winLosRatio']
    fraction = settings['fraction']
    myRuin = settings['myRuin']
    langID = settings['langID']
    histBinsCount = settings['histBinsCount']

    data, mdds = dict(), dict()
    mdds['MDD'], mdds['Ruin'], mdds['FinCap'] = list(), list(), list()

    for s in range(simulationsCount):
        eqCurve = list()
        eqCurve.append(1)
        for x in range(1, tradesCount + 1):
            randNum = random.random()
            if randNum < winRate:   # WINNER
                appendValue = eqCurve[x - 1] * (1 + fraction * winLosRatio)
            else:                   # LOSER
                appendValue = eqCurve[x - 1] * (1 - fraction)
            eqCurve.append(appendValue)
        data[s] = eqCurve

        mdf = pd.DataFrame(data[s])
        mdf.rename(columns = {0: 'Equity'}, inplace=True)
        mdf['HWM'] = mdf['Equity'].cummax()
        mdf['DD'] = 1 - mdf['Equity'] / mdf['HWM']
        thisMDD = max(mdf['DD'])

        mdds['MDD'].append(thisMDD)
        mdds['Ruin'].append(thisMDD >= myRuin)
        mdds['FinCap'].append(data[s][-1])

    dfmdds = pd.DataFrame(mdds)
    riskOfRuin = sum(dfmdds['Ruin']) / simulationsCount

    textsENRU = {'Title': ['Monte Carlo Generator', 'Генератор Монте-Карло'],
                 'Simulations': ['Simulations', 'Симуляций'],
                 'Trades': ['Trades', 'Сделок'],
                 'Random curves': ['Random curves', 'Случайных кривых'],
                 'Win Rate': ['Win Rate', 'Прибыльных'],
                 'W/L ratio': ['W/L ratio', 'Приб/убыт'],
                 'Fraction': ['Fraction', 'Фракция'],
                 'Ruin': ['Ruin', 'Max Потеря'],
                 'Risk of ruin': ['Risk of ruin', 'Риск потери'],
                 'xlabel': ['Trades', 'Сделки'],
                 'ylabel': ['Capital', 'Капитал'],
                 'MDD distribution': ['MDD distribution', 'Распределение MDD'],
                 'FinRes distribution': ['FinResult distribution', 'Распределение ФинРез'],
                 'Mean': ['Mean', 'Среднее'],
                 'Median': ['Median', 'Медиана']}
    textBoxInside = f'{textsENRU["Simulations"][langID]}: {simulationsCount}\n' \
                    f'{textsENRU["Random curves"][langID]}: {randomCurves}\n\n' \
                    f'{textsENRU["Trades"][langID]}: {tradesCount}\n' \
                    f'{textsENRU["Win Rate"][langID]}: {winRate * 100:.1f}%\n' \
                    f'{textsENRU["W/L ratio"][langID]}: {winLosRatio:.1f}\n' \
                    f'{textsENRU["Fraction"][langID]}: {fraction * 100:.2f}%\n' \
                    f'{textsENRU["Ruin"][langID]}: {myRuin * 100:.1f}%\n\n' \
                    f'{textsENRU["Risk of ruin"][langID]}: {riskOfRuin * 100:.1f}%'
    df1 = pd.DataFrame(data)
    df = df1[random.sample(range(simulationsCount), randomCurves)]
    maxVal = df.max().max()

    distrMDDs = dfmdds['MDD']
    distrFinCaps = dfmdds['FinCap']

    fig = plt.figure(constrained_layout=True, figsize=(9, 6.5))
    gs = fig.add_gridspec(2, 2)

    f_ax1 = fig.add_subplot(gs[0, :])
    f_ax1.set_title(textsENRU['Title'][langID], fontweight='bold')
    f_ax1.set_xlabel(textsENRU['xlabel'][langID], fontweight='bold')
    f_ax1.set_ylabel(textsENRU['ylabel'][langID], fontweight='bold')
    f_ax1.set_yscale('log')
    props = dict(boxstyle='round', alpha=0.5)  # facecolor='wheat'
    f_ax1.text(0, maxVal, textBoxInside, verticalalignment='top', bbox=props)
    f_ax1.plot(df)

    f_ax2 = fig.add_subplot(gs[1, 0])
    f_ax2.set_title(textsENRU['MDD distribution'][langID], fontweight='bold')
    f_ax2.hist(distrMDDs, bins=histBinsCount)
    meanMDD, medianMDD = distrMDDs.mean(), distrMDDs.median()
    f_ax2.axvline(meanMDD, color='k', linestyle='dashed', linewidth=1)
    mddTextBox = f"{textsENRU['Mean'][langID]}: {meanMDD * 100:.1f}%\n" \
                 f"{textsENRU['Median'][langID]}: {medianMDD * 100:.1f}%"
    f_ax2.text(0.05, 0.95, mddTextBox, transform=f_ax2.transAxes, verticalalignment='top', bbox=props)

    f_ax3 = fig.add_subplot(gs[1, 1])
    f_ax3.set_title(textsENRU['FinRes distribution'][langID], fontweight='bold')
    f_ax3.hist(distrFinCaps, bins=histBinsCount)
    meanFinRes, medianFinRes = distrFinCaps.mean(), distrFinCaps.median()
    f_ax3.axvline(meanFinRes, color='k', linestyle='dashed', linewidth=1)
    finresTextBox = f"{textsENRU['Mean'][langID]}: {meanFinRes:.3f}\n" \
                    f"{textsENRU['Median'][langID]}: {medianFinRes:.3f}"
    f_ax3.text(0.05, 0.95, finresTextBox, transform=f_ax3.transAxes, verticalalignment='top', bbox=props)

    # fig.savefig('pypl_img01.png')
    plt.show()