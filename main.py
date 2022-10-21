import json
import sys
import tkinter as tk

from simulation import run_mc_single as run_mc


def on_exit():
    root.destroy()
    sys.exit()


def click_btn_start():
    # update mySettings dictionary

    updated_settings = {
        'simulations count': int(entry_simulations.get()),
        'random curves': int(ent_rand_curves.get()),
        'trades count': int(ent_trades_count.get()),
        'win rate': float(ent_win_rate.get()),
        'win loss ratio': float(ent_win_loss_ratio.get()),
        'fraction': float(ent_fraction.get()),
        'my ruin': float(ent_my_ruin.get()),
        'lang id': int(ent_lang_id.get()),
        'bins count': int(ent_bins_count.get())
    }

    with open(settings_file, 'w') as f:
        json.dump(updated_settings, f, indent=4)

    # pass to function runGenerator()
    run_mc(updated_settings)


# READ SETTINGS
settings_file = 'settings.json'
with open(settings_file, 'r') as f_obj:
    my_settings = json.load(f_obj)

gui_labels = {
    'Title': ['Empirix.ru: Monte Carlo Generator',
              'Empirix.ru: Генератор Монте-Карло'],
    'Settings': ['Settings', 'Настройки'],
    'Simulations': ['Simulations', 'Симуляций'],
    'Random curves': ['Random curves', 'Случайных кривых'],
    'Trades': ['Trades', 'Сделок'],
    'Win Rate': ['Win Rate', 'Прибыльных'],
    'W/L ratio': ['W/L ratio', 'Приб/убыт'],
    'Fraction': ['Fraction', 'Фракция'],
    'Ruin': ['Ruin', 'Max Потеря'],
    'lang id': ['lang id (0=EN, 1=RU)', 'ID языка (0=EN, 1=RU)'],
    'Hist bins': ['Histogram bins', 'Гистограмма, бинов'],
    'Start': ['Start', 'Пуск'],
    'Quit': ['Quit', 'Выход'],
}

root = tk.Tk()
root.title(gui_labels['Title'][my_settings['lang id']])
root.geometry('400x320')
root.resizable(False, False)

# Frame 1. Settings
frame_settings = tk.LabelFrame(
    master=root,
    text=f"{gui_labels['Settings'][my_settings['lang id']]}",
    padx=7,
    pady=7
)
frame_settings.pack()

label_width = 20
entry_width = 10

lbl_simulations = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Simulations'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W)
lbl_simulations.grid(row=0, column=0)

entry_simulations = tk.Entry(frame_settings, width=entry_width)
entry_simulations.grid(row=0, column=1)
entry_simulations.insert(0, my_settings['simulations count'])

lbl_rand_curves = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Random curves'][my_settings['lang id']]}",
    width=label_width, anchor=tk.W
)
lbl_rand_curves.grid(row=1, column=0)

ent_rand_curves = tk.Entry(master=frame_settings, width=entry_width)
ent_rand_curves.grid(row=1, column=1)
ent_rand_curves.insert(0, my_settings['random curves'])

lbl_trades_count = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Trades'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)
lbl_trades_count.grid(row=2, column=0)

ent_trades_count = tk.Entry(master=frame_settings, width=entry_width)
ent_trades_count.grid(row=2, column=1)
ent_trades_count.insert(0, my_settings['trades count'])

lbl_win_rate = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Win Rate'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)
lbl_win_rate.grid(row=3, column=0)

ent_win_rate = tk.Entry(master=frame_settings, width=entry_width)
ent_win_rate.grid(row=3, column=1)
ent_win_rate.insert(0, my_settings['win rate'])

lbl_win_loss_ratio = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['W/L ratio'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)

lbl_win_loss_ratio.grid(row=4, column=0)

ent_win_loss_ratio = tk.Entry(master=frame_settings, width=entry_width)
ent_win_loss_ratio.grid(row=4, column=1)
ent_win_loss_ratio.insert(0, my_settings['win loss ratio'])

lbl_fraction = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Fraction'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)
lbl_fraction.grid(row=5, column=0)

ent_fraction = tk.Entry(master=frame_settings, width=entry_width)
ent_fraction.grid(row=5, column=1)
ent_fraction.insert(0, my_settings['fraction'])

lbl_my_ruin = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Ruin'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)
lbl_my_ruin.grid(row=6, column=0)

ent_my_ruin = tk.Entry(master=frame_settings, width=entry_width)
ent_my_ruin.grid(row=6, column=1)
ent_my_ruin.insert(0, my_settings['my ruin'])

lbl_lang_id = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['lang id'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)
lbl_lang_id.grid(row=7, column=0)

ent_lang_id = tk.Entry(master=frame_settings, width=entry_width)
ent_lang_id.grid(row=7, column=1)
ent_lang_id.insert(0, my_settings['lang id'])

lbl_bins_count = tk.Label(
    master=frame_settings,
    text=f"{gui_labels['Hist bins'][my_settings['lang id']]}",
    width=label_width,
    anchor=tk.W
)
lbl_bins_count.grid(row=8, column=0)

ent_bins_count = tk.Entry(master=frame_settings, width=entry_width)
ent_bins_count.grid(row=8, column=1)
ent_bins_count.insert(0, my_settings['bins count'])

# BUTTONS
btn_start = tk.Button(
    master=root,
    text=f"{gui_labels['Start'][my_settings['lang id']]}",
    command=click_btn_start,
    width=12,
    height=3
)
btn_start.pack()
# buttonStart.grid(row=1, column=0)
# buttonQuit = Button(root, text=f"{tkTexts['Quit'][mySettings['lang id']]}",
# command=root.destroy)
# buttonQuit.grid(row=1, column=1)

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
