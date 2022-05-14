import matplotlib.pyplot as plt
import pandas as pd
import random

from datetime import datetime
from PIL import Image


def run_mc_single(settings):
    simulations_count = settings['simulations count']
    random_curves = settings['random curves']
    trades_count = settings['trades count']
    win_rate = settings['win rate']
    win_loss_ratio = settings['win loss ratio']
    fraction = settings['fraction']
    my_ruin = settings['my ruin']
    lang_id = settings['lang id']
    bins_count = settings['bins count']

    data, mdds = dict(), dict()
    mdds['MDD'], mdds['Ruin'], mdds['FinCap'] = list(), list(), list()

    for s in range(simulations_count):
        eq_curve = list()
        eq_curve.append(1)
        for x in range(1, trades_count + 1):
            rand_num = random.random()

            if rand_num < win_rate:
                # WINNER!
                append_value = eq_curve[x - 1] \
                               * (1 + fraction * win_loss_ratio)
            else:
                # LOSER!
                append_value = eq_curve[x - 1] * (1 - fraction)

            eq_curve.append(append_value)
        data[s] = eq_curve

        mdf = pd.DataFrame(data[s])
        mdf.rename(columns={0: 'Equity'}, inplace=True)
        mdf['HWM'] = mdf['Equity'].cummax()
        mdf['DD'] = 1 - mdf['Equity'] / mdf['HWM']
        this_mdd = max(mdf['DD'])

        mdds['MDD'].append(this_mdd)
        mdds['Ruin'].append(this_mdd >= my_ruin)
        mdds['FinCap'].append(data[s][-1])

    df_mdds = pd.DataFrame(mdds)
    risk_of_ruin = sum(df_mdds['Ruin']) / simulations_count

    texts_en_ru = {
        'Title': ['Monte Carlo Generator', 'Генератор Монте-Карло'],
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
        'FinRes distribution': ['FinResult distribution',
                                'Распределение ФинРез'],
        'Mean': ['Mean', 'Среднее'],
        'Median': ['Median', 'Медиана'],
    }

    text_box_inside = \
        f'{texts_en_ru["Simulations"][lang_id]}: {simulations_count}\n' \
        f'{texts_en_ru["Random curves"][lang_id]}: {random_curves}\n\n' \
        f'{texts_en_ru["Trades"][lang_id]}: {trades_count}\n' \
        f'{texts_en_ru["Win Rate"][lang_id]}: {win_rate * 100:.1f}%\n' \
        f'{texts_en_ru["W/L ratio"][lang_id]}: {win_loss_ratio:.1f}\n' \
        f'{texts_en_ru["Fraction"][lang_id]}: {fraction * 100:.2f}%\n' \
        f'{texts_en_ru["Ruin"][lang_id]}: {my_ruin * 100:.1f}%\n\n' \
        f'{texts_en_ru["Risk of ruin"][lang_id]}: {risk_of_ruin * 100:.1f}%'

    df1 = pd.DataFrame(data)
    df = df1[random.sample(range(simulations_count), random_curves)]
    max_val = df.max().max()

    distr_mdds = df_mdds['MDD']
    distr_fin_caps = df_mdds['FinCap']

    fig = plt.figure(constrained_layout=True, figsize=(9, 6.5))
    gs = fig.add_gridspec(2, 2)

    f_ax1 = fig.add_subplot(gs[0, :])
    f_ax1.set_title(texts_en_ru['Title'][lang_id], fontweight='bold')
    f_ax1.set_xlabel(texts_en_ru['xlabel'][lang_id], fontweight='bold')
    f_ax1.set_ylabel(texts_en_ru['ylabel'][lang_id], fontweight='bold')
    f_ax1.set_yscale('log')
    props = dict(boxstyle='round', alpha=0.5)  # facecolor='wheat'
    f_ax1.text(0, max_val, text_box_inside, verticalalignment='top',
               bbox=props)
    f_ax1.plot(df)

    f_ax2 = fig.add_subplot(gs[1, 0])
    f_ax2.set_title(texts_en_ru['MDD distribution'][lang_id],
                    fontweight='bold')
    f_ax2.hist(distr_mdds, bins=bins_count)

    mean_mdd, median_mdd = distr_mdds.mean(), distr_mdds.median()

    f_ax2.axvline(mean_mdd, color='k', linestyle='dashed', linewidth=1)

    mdd_text_box = \
        f"{texts_en_ru['Mean'][lang_id]}: {mean_mdd * 100:.1f}%\n" \
        f"{texts_en_ru['Median'][lang_id]}: {median_mdd * 100:.1f}%"

    f_ax2.text(0.05, 0.95, mdd_text_box, transform=f_ax2.transAxes,
               verticalalignment='top', bbox=props)

    f_ax3 = fig.add_subplot(gs[1, 1])
    f_ax3.set_title(texts_en_ru['FinRes distribution'][lang_id],
                    fontweight='bold')
    f_ax3.hist(distr_fin_caps, bins=bins_count)

    mean_fin_res = distr_fin_caps.mean()
    median_fin_res = distr_fin_caps.median()

    f_ax3.axvline(mean_fin_res, color='k', linestyle='dashed', linewidth=1)

    fin_res_text_box = \
        f"{texts_en_ru['Mean'][lang_id]}: {mean_fin_res:.3f}\n" \
        f"{texts_en_ru['Median'][lang_id]}: {median_fin_res:.3f}"

    f_ax3.text(0.05, 0.95, fin_res_text_box, transform=f_ax3.transAxes,
               verticalalignment='top', bbox=props)

    n = datetime.now()
    img_path = f"images/img_{n.year:02d}{n.month:02d}{n.day:02d}" \
               f"_{n.hour:02d}{n.minute:02d}{n.second:02d}.png"
    fig.savefig(img_path)

    im = Image.open(img_path)
    im.show()

    # plt.show()
