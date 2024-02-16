import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager

# Constants for column names
PROJECT_COLUMN = 'Project'
CARBON_REDUCTION = 'Scale'
MARGINAL_COSTS_COLUMN = 'Marginal Costs'
X_POS_COLUMN = 'xpos'

# Load data from CSV file
df = pd.read_csv('data.csv')

# Sort DataFrame by 'Marginal Costs' in ascending order
df = df.sort_values(by=MARGINAL_COSTS_COLUMN, ascending=True).reset_index(drop=True)

df[X_POS_COLUMN] = 0.0  # Initialize the xpos column with floating point zeros for accuracy

for index in range(len(df)):
    if index == 0:
        df.loc[index, X_POS_COLUMN] = df.loc[index, CARBON_REDUCTION] / 2
    else:
        df.loc[index, X_POS_COLUMN] = df.loc[index, CARBON_REDUCTION] / 2 + df.loc[index - 1, X_POS_COLUMN] + df.loc[
            index - 1, CARBON_REDUCTION] / 2


def merit_order_curve():
    plt.figure(figsize=(20, 12))
    plt.rcParams["font.size"] = 16

    colors = ["#e26c38", "#a7a7a7", "#5f6269"]
    xpos = df[X_POS_COLUMN].values.tolist()
    y = df[MARGINAL_COSTS_COLUMN].values.tolist()
    w = df[CARBON_REDUCTION].values.tolist()

    fig = plt.bar(xpos, height=y, width=w, fill=True, color=colors)

    plt.xlim(0, df[CARBON_REDUCTION].sum())
    plt.ylim(df[MARGINAL_COSTS_COLUMN].min() - 20, df[MARGINAL_COSTS_COLUMN].max() + 20)

    ax = plt.gca()
    fmtr = matplotlib.ticker.StrMethodFormatter('{x:,.0f}')
    ax.xaxis.set_major_formatter(fmtr)

    font_dirs = ['/Users/greg/Library/Fonts/']
    font_files = matplotlib.font_manager.findSystemFonts(fontpaths=font_dirs, fontext='ttf')
    for font_file in font_files:
        matplotlib.font_manager.fontManager.addfont(font_file)

    # specify the custom font to use
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Exo 2'

    plt.xlabel("Cumulative MT CO2")
    plt.ylabel("$/MT CO2")
    plt.show()

merit_order_curve()
