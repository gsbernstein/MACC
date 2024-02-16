import matplotlib.pyplot as plt
import pandas as pd

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

    colors = ["yellow", "limegreen", "skyblue", "pink", "limegreen", "black", "orange", "grey", "maroon"]
    xpos = df[X_POS_COLUMN].values.tolist()
    y = df[MARGINAL_COSTS_COLUMN].values.tolist()
    w = df[CARBON_REDUCTION].values.tolist()

    fig = plt.bar(xpos, height=y, width=w, fill=True, color=colors)

    plt.xlim(0, df[CARBON_REDUCTION].sum())
    plt.ylim(0, df[MARGINAL_COSTS_COLUMN].max() + 20)

    # projects = df[PROJECT_COLUMN].values.tolist()
    # plt.legend(fig.patches, projects, loc="upper left", ncol=1)

    plt.xlabel("Cumulative MT CO2")
    plt.ylabel("$/MT CO2")
    plt.show()

merit_order_curve()
