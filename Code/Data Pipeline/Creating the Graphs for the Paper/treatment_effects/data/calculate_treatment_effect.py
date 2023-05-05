import pandas as pd
import os
import sys

def calculate_treatment_effect(y_post, y_star_post):
    time_units = len(y_post)
    diff = 0
    for i in range(len(y_post)):
        diff += y_post[i] - y_star_post[i]
    effect = diff / time_units
    # Round the effect to 2 places after the comma {.2f}
    print(format(effect, ".2f"))
    return effect


def fix_synth_date(df, canton):
    for i in range(len(df)):
        if df.loc[i, "canton"] == f'synth_{canton}':
            df.loc[i, "month"] = df.loc[i - 1, "month"]
    return df


def get_formatted_df_for_cutoff(cutoff, case):
    master_df = pd.DataFrame(columns=['month', 'days'])
    # Iterate through all folder in the "A1.0" directory
    path = f'case_{case}/controlled_for_taxes/ZG/{cutoff}_synth_ZG.csv' 
    df = pd.read_csv(path)
    df = df[["month", "canton", "companies", "days"]]
    # Select only the rows where the canton is ZG or synth_ZG
    df = df[df["canton"].isin([f'ZG', f'synth_ZG'])]
    # Reset the index
    df = df.reset_index(drop=True)
    df = fix_synth_date(df, canton="ZG")
    # Convert the "month" column to a datetime format
    df["month"] = pd.to_datetime(df["month"])
    # Define the order of the cantons
    canton_order = [f'ZG', f'synth_ZG']
    # Convert the "canton" column to a categorical with the specified order
    df["canton"] = pd.Categorical(df["canton"], categories=canton_order, ordered=True)
    # Reshape the DataFrame so that the canton disappears, and instead, there is a Y column for all companies where canton = ZG and Y_star for canton = synth_ZG
    df = df.pivot(index=["month", "days"], columns="canton", values="companies").reset_index()
    # Rename the columns
    df.columns = ["month", "days", f'Y', f'Y_star']
    df["month"] = pd.to_datetime(df["month"])
    master_df = master_df.merge(df[['month', 'days', f'Y', f'Y_star']], on=['month', 'days'], how='outer')
    # order by days (ascending)
    master_df = master_df.sort_values(by=['days'], ascending=True)
    master_df = master_df.reset_index(drop=True)
    return master_df


def make_all_formatted_dfs():
    master_df = pd.DataFrame()
    for case in range(0, 5):
        for cutoff in range(0, 21):
            df = get_formatted_df_for_cutoff(cutoff, case)
            df["case"] = case
            df["cutoff"] = cutoff
            print(cutoff, case)
            master_df = master_df.append(df)
    return master_df


def make_treatment_df(master_df):
    treatment_df = pd.DataFrame(columns=["case", "cutoff", "treatment_effect"])
    for case in range(0, 5):
        for cutoff in range(0, 21):
            df = master_df[(master_df["case"] == case) & (master_df["cutoff"] == cutoff) & (master_df["days"] > 1796)]
            y_post = df["Y"].values
            y_star_post = df["Y_star"].values
            treatment_effect = calculate_treatment_effect(y_post, y_star_post)
            treatment_df = treatment_df.append({"case": case, "cutoff": cutoff, "treatment_effect": treatment_effect}, ignore_index=True)
    return treatment_df

master_df = make_all_formatted_dfs()
treatment_df = make_treatment_df(master_df)
treatment_df.to_csv("treatment_df.csv", index=False)
# master_df.to_csv("formatted_df.csv", index=False)            






# TO CALCULATE THE TREATMENT EFFECT
# df = pd.read_csv('formatted_0_ZG_df.csv')


# # Select only rows where day > 1796
# df = df[df['days'] > 1796]

# # Turn the column Y_star into a list
# y_star = df["Y_star"].values
# y = df["Y"].values
# calculate_treatment_effect(y, y_star)
