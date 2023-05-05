import pandas as pd
import os
import sys


def fix_synth_date(df, canton):
    for i in range(len(df)):
        if df.loc[i, "canton"] == f'synth_{canton}':
            df.loc[i, "month"] = df.loc[i - 1, "month"]
    return df


def get_formatted_df_for_cutoff(cutoff):
    master_df = pd.DataFrame(columns=['month', 'days'])
    # Iterate through all folder in the "A1.0" directory
    for folder in os.listdir("A1.0"):
        # get the foldername
        foldername = folder
        try:
            df = pd.read_csv("A1.0/" + foldername + f'/{cutoff}_synth_{foldername}.csv')
        except:
            print(f'No data for {foldername} with cutoff {cutoff} found')
            continue
        df = df[["month", "canton", "companies", "days"]]
        # Select only the rows where the canton is ZG or synth_ZG
        df = df[df["canton"].isin([f'{foldername}', f'synth_{foldername}'])]
        # Reset the index
        df = df.reset_index(drop=True)
        df = fix_synth_date(df, canton=foldername)
        # Convert the "month" column to a datetime format
        df["month"] = pd.to_datetime(df["month"])
        # Define the order of the cantons
        canton_order = [f'{foldername}', f'synth_{foldername}']
        # Convert the "canton" column to a categorical with the specified order
        df["canton"] = pd.Categorical(df["canton"], categories=canton_order, ordered=True)
        # Reshape the DataFrame so that the canton disappears, and instead, there is a Y column for all companies where canton = ZG and Y_star for canton = synth_ZG
        df = df.pivot(index=["month", "days"], columns="canton", values="companies").reset_index()
        # Rename the columns
        df.columns = ["month", "days", f'Y_{foldername}', f'Y_star_{foldername}']
        df["month"] = pd.to_datetime(df["month"])
        print(df.tail())
        master_df = master_df.merge(df[['month', 'days', f'Y_{foldername}', f'Y_star_{foldername}']], on=['month', 'days'], how='outer')
    return master_df

# cutoff = 0
# master_df = get_formatted_df_for_cutoff(cutoff=cutoff)
# master_df.to_csv(f'master_df_{cutoff}.csv', index=False)
