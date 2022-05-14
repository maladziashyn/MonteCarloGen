# MonteCarloGen

A tool for financial market **traders**.

Monte Carlo generator that helps estimate **RISK OF RUIN**.

Measure your back-test KPIs (such as "win ratio", "average winner to average 
loser ratio", "trades count"), stick them into the generator and get the value
of "Risk of ruin".

`random` module is used to generate trades.

## User guide

1. Run the app
2. Fill in the "Settings" fields
3. Press "Start"

### "Settings" fields

* **Simulations** (int) - how many simulations will be run
* **Random curves** (int) - how many random equity curves will be displayed on the resulting image
* **Trades** (int) - trades count in one simulation
* **Win Rate** (float) - ratio of winning trades (e.g. 0.431 means 43.1% winning trades)
* **W/L Ratio** (float) - "average winner" to "average loser" ratio, i.e. average winner is *X* times greater than the average loser
* **Fraction** (float) - fraction of the account balance lost in case the trade is a loser (0.01 means 1%)
* **Ruin** (float) - your risk tolerance level, i.e. 0.2 means that the simulation is considered a failure if the account balance decreases at least 20%
* **lang id** - choose your language
* **Histogram bins** - number of bins for each histogram in the report

## Report

The report includes 3 images:

### 1. Equity curves 

Topmost image shows some random curves from the whole batch of simulations.

Simulation settings and the resulting Risk of Ruin are show in the top 
left-hand corner.

### 2. MDD distribution

Maximum draw-down (MDD) distribution histogram with the pre-defined number of 
bins. Also shows mean and median MDD.

### 3. FinResult distribution

Financial result (FinRes) distribution historgam with the pre-defined number of 
bins. Also shows mean and median FinRes.

### Report, images

The report shows as an image. Each simulation generates an image. The images 
are saved in "images" folder, so every once in a while do a clean-up there :)

**Have fun!**