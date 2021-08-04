import json
from tkinter import *
from MC_gen_single import runMCSingle as runMC

def clickButtonStart():
    # update mySettings dictionary

    updatedSettings = {
        'simulationsCount': int(entrySimulations.get()),
        'randomCurves': int(entryRandomCurves.get()),
        'tradesCount': int(entryTradesCount.get()),
        'winRate': float(entryWinRate.get()),
        'winLosRatio': float(entryWinLosRatio.get()),
        'fraction': float(entryFraction.get()),
        'myRuin': float(entryMyRuin.get()),
        'langID': int(entryLangID.get()),
        'histBinsCount': int(entryHistBinsCount.get())
    }
    with open(settingsFName, 'w') as fObj:
        json.dump(updatedSettings, fObj, indent=4)
    # pass to function runGenerator()
    runMC(updatedSettings)

# READ SETTINGS
settingsFName = 'MC_gen_settings.json'
with open(settingsFName, 'r') as fObj:
    mySettings = json.load(fObj)


tkTexts = {'Title': ['VSAtrader.ru: Monte Carlo Generator', 'VSAtrader.ru: Генератор Монте-Карло'],
                     'Settings': ['Settings', 'Настройки'],
                     'Simulations': ['Simulations', 'Симуляций'],
                     'Random curves': ['Random curves', 'Случайных кривых'],
                     'Trades': ['Trades', 'Сделок'],
                     'Win Rate': ['Win Rate', 'Прибыльных'],
                     'W/L ratio': ['W/L ratio', 'Приб/убыт'],
                     'Fraction': ['Fraction', 'Фракция'],
                     'Ruin': ['Ruin', 'Max Потеря'],
                     'LangID': ['LangID (0=EN, 1=RU)', 'ID языка (0=EN, 1=RU)'],
                     'Hist bins': ['Histogram bins', 'Гистограмма, бинов'],
                     'Start': ['Start', 'Пуск'],
                     'Quit': ['Quit', 'Выход']}

root = Tk()
root.title(tkTexts['Title'][mySettings['langID']])
root.geometry('400x320')
# root.iconbitmap('vsatrader_icon.ico')
root.resizable(False, False)

# Frame 1. Settings
frameSettings = LabelFrame(root, text=f"{tkTexts['Settings'][mySettings['langID']]}", padx=7, pady=7)
# frameSettings.grid(row=0, column=0)
frameSettings.pack()

lbWidth = 20
entryWidth = 10

lbSimulations = Label(frameSettings, text=f"{tkTexts['Simulations'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbSimulations.grid(row=0, column=0)
entrySimulations = Entry(frameSettings, width=entryWidth)
entrySimulations.grid(row=0, column=1)
entrySimulations.insert(0, mySettings['simulationsCount'])

lbRandomCurves = Label(frameSettings, text=f"{tkTexts['Random curves'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbRandomCurves.grid(row=1, column=0)
entryRandomCurves = Entry(frameSettings, width=entryWidth)
entryRandomCurves.grid(row=1, column=1)
entryRandomCurves.insert(0, mySettings['randomCurves'])

lbTradesCount = Label(frameSettings, text=f"{tkTexts['Trades'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbTradesCount.grid(row=2, column=0)
entryTradesCount = Entry(frameSettings, width=entryWidth)
entryTradesCount.grid(row=2, column=1)
entryTradesCount.insert(0, mySettings['tradesCount'])

lbWinRate = Label(frameSettings, text=f"{tkTexts['Win Rate'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbWinRate.grid(row=3, column=0)
entryWinRate = Entry(frameSettings, width=entryWidth)
entryWinRate.grid(row=3, column=1)
entryWinRate.insert(0, mySettings['winRate'])

lbWinLosRatio = Label(frameSettings, text=f"{tkTexts['W/L ratio'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbWinLosRatio.grid(row=4, column=0)
entryWinLosRatio = Entry(frameSettings, width=entryWidth)
entryWinLosRatio.grid(row=4, column=1)
entryWinLosRatio.insert(0, mySettings['winLosRatio'])

lbFraction = Label(frameSettings, text=f"{tkTexts['Fraction'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbFraction.grid(row=5, column=0)
entryFraction = Entry(frameSettings, width=entryWidth)
entryFraction.grid(row=5, column=1)
entryFraction.insert(0, mySettings['fraction'])

lbMyRuin = Label(frameSettings, text=f"{tkTexts['Ruin'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbMyRuin.grid(row=6, column=0)
entryMyRuin = Entry(frameSettings, width=entryWidth)
entryMyRuin.grid(row=6, column=1)
entryMyRuin.insert(0, mySettings['myRuin'])

lbLangID = Label(frameSettings, text=f"{tkTexts['LangID'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbLangID.grid(row=7, column=0)
entryLangID = Entry(frameSettings, width=entryWidth)
entryLangID.grid(row=7, column=1)
entryLangID.insert(0, mySettings['langID'])

lbHistBinsCount = Label(frameSettings, text=f"{tkTexts['Hist bins'][mySettings['langID']]}", width=lbWidth, anchor=W)
lbHistBinsCount.grid(row=8, column=0)
entryHistBinsCount = Entry(frameSettings, width=entryWidth)
entryHistBinsCount.grid(row=8, column=1)
entryHistBinsCount.insert(0, mySettings['histBinsCount'])

# BUTTONS
buttonStart = Button(root, text=f"{tkTexts['Start'][mySettings['langID']]}", command=clickButtonStart,
                     width=12, height=3)
buttonStart.pack()
# buttonStart.grid(row=1, column=0)
# buttonQuit = Button(root, text=f"{tkTexts['Quit'][mySettings['langID']]}", command=root.destroy)
# buttonQuit.grid(row=1, column=1)


root.mainloop()