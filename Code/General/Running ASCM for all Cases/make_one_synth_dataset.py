import pandas as pd
import matplotlib as plot
import matplotlib.pyplot as plt
import seaborn as sns

def get_weighted_value(weights, day_df, col):
    value = 0
    for index, row in day_df.iterrows():
        canton = row["canton"]
        weight_row = weights[weights["canton"] == canton]
        try:
            value += row[col] * weight_row["weights"].values[0]
        except:
            pass
    return value


def save_synth_df(industry, weights, canton, file_path):
    # industry = pd.read_csv("aggregated_industry_data.csv")
    # weights = pd.read_csv("weights.csv")
    days = industry["days"].unique()
    all_days_df = pd.DataFrame()
    for day in days:
        day_df = industry[industry["days"] == day]
        companies = get_weighted_value(weights, day_df, "companies")
        row = {"canton": f'synth_{canton}', "companies": companies, "days": day}
        # Append the row to the day_df
        day_df = day_df.append(row, ignore_index = True)
        all_days_df = all_days_df.append(day_df)

    # Save to CSV
    all_days_df.to_csv(file_path, index=False)
